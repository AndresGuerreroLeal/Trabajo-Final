let colo=document.querySelector('#precios')
const carrito = document.querySelector("#lista-carrito");
const contenedorCarrito = document.querySelector("#lista-carrito tbody");
const vaciarCarritoBtn = document.querySelector("#vaciar-carrito");
let articulosCarrito = [];
console.log(document.querySelector("#imagen").value);
console.log(contenedorCarrito);
// Listeners
document.addEventListener("DOMContentLoaded", () => {
  articulosCarrito = JSON.parse(localStorage.getItem("carrito")) || [];
  // console.log(articulosCarrito);
  carritoHTML();
});

cargarEventListeners();

function cargarEventListeners() {
  // Dispara cuando se presiona "Agregar Carrito"

  document.addEventListener("DOMContentLoaded", leerDatosCurso);
  document.addEventListener("DOMContentLoaded", precios);
  // Cuando se elimina un curso del carrito
  carrito.addEventListener("click", eliminarCurso);

  // Al Vaciar el carrito
  vaciarCarritoBtn.addEventListener("click", vaciarCarrito);

  // NUEVO: Contenido cargado
}

// Función que añade el curso al carrito

// Lee los datos del curso
function leerDatosCurso() {
  const infoCurso = {
    imagen: document.querySelector("#imagen").value,
    titulo: document.querySelector("#articulo").value,
    precio: document.querySelector("#precio").value,
    descri: document.querySelector("#descri").value,
    id: document.querySelector("#id").value,
    cantidad: 1,
  };

  if (articulosCarrito.some((curso) => curso.id === infoCurso.id)) {
    const cursos = articulosCarrito.map((curso) => {
      if (curso.id === infoCurso.id) {
        let cantidad = parseInt(curso.cantidad);
        cantidad++;
        curso.cantidad = cantidad;
        return curso;
      } else {
        return curso;
      }
    });
    articulosCarrito = [...cursos];
  } else {
    articulosCarrito = [...articulosCarrito, infoCurso];
  }

  console.log(articulosCarrito);

  // console.log(articulosCarrito)
  carritoHTML();
}
function precios() {

  let total = articulosCarrito.map((curso) => {
    let total = curso.precio * curso.cantidad;
    return total;
  });
  let resultado = [...total];
  resultado.reduce((a, b) => {
    return a + b, 0;
  });

  
  let precio=resultado[0].toFixed(3)
  
  colo.textContent=precio

}

// Elimina el curso del carrito en el DOM
function eliminarCurso(e) {
  // e.preventDefault();
  vaciarCarrito();
  // if(e.target.classList.contains('borrar-curso') ) {
  //      // e.target.parentElement.parentElement.remove();

  //      const curso = document.querySelector('.borrar-curso')

  //      const cursoId = curso.getAttribute('data-id');

  //      // Eliminar del arreglo del carrito
  //      articulosCarrito = articulosCarrito.filter(curso => curso.id !== cursoId);

  //      carritoHTML();
  // }
}

// Muestra el curso seleccionado en el Carrito
function carritoHTML() {
  vaciarCarrito();

  articulosCarrito.forEach((curso) => {
    const row = document.createElement("tr");
    row.innerHTML = `
          <td>  
          <img src="${curso.imagen}" style="width:150px;border-radius:10px;">
          </td>
          <td>${curso.titulo}</td>
          <td>${curso.id}</td>
          <td>${curso.descri}</td>
          <td>${curso.cantidad} </td>
          <td>${curso.precio}</td>
          <td><i class="fas fa-trash-alt borrar-curso" data-id="{{ curso.id }}"  style="cursor: pointer;"></i></td>
          `;
    contenedorCarrito.appendChild(row);
  });

  // NUEVO:
  sincronizarStorage();
}

// NUEVO:
function sincronizarStorage() {
  localStorage.setItem("carrito", JSON.stringify(articulosCarrito));
}

// Elimina los cursos del carrito en el DOM
function vaciarCarrito() {
  // forma rapida (recomendada)
  while (contenedorCarrito.firstChild) {
    contenedorCarrito.removeChild(contenedorCarrito.firstChild);
  }
  colo.textContent=0;
}

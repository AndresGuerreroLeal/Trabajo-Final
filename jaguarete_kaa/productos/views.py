

from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .forms import NuevoForm
from .models import nuevo
# Create your views here.

def producto(request):
     if request.GET["prd"]:
        producto=request.GET['prd']

        articulo=nuevo.objects.filter(pk__icontains=producto)
        
        return render(request,"./compras/producto.html",
        {"articulos":articulo,"query":producto})

     else:
        mensaje='No has introduccido nada'

     return render(request,'./compras/producto.html')
    # productos=nuevo.objects.all().order_by('created')

    # return render(request,'./compras/producto.html',{'productos':productos})

   

    

@login_required
def editar(request):
    traer=request.GET['prd']
    producto=get_object_or_404(nuevo,nombre=traer)

    articulos=nuevo.objects.filter(nombre__icontains=traer)
    data={
        'form':NuevoForm(instance=producto),
        'articulos':articulos
    }
    
    if request.method=='POST':
        form=NuevoForm(request.POST,request.FILES,instance=producto)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    return render(request,'./compras/editar.html',data)


@login_required
def eliminar(request):
    traer=request.GET['prd']
    producto=get_object_or_404(nuevo,nombre=traer)
    producto.delete()
    return redirect('home')

@login_required
def crear(request):
    productos=nuevo.objects.all().order_by('-created')
    if request.method=='POST':
        form=NuevoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=NuevoForm()
    

    return render(request,'./compras/crear.html',context={'form':form,'profile':request.user.perfil,'user':request.user})

def home(request):
    productos=nuevo.objects.all().order_by('-id')[:3]
    productoCaja=nuevo.objects.all().order_by('-id')[3:]
    return render(request,"./producto/home.html",{'productos':productos,'productoCaja':productoCaja})

def busqueda_productos(request):
    if request.GET["prd"]:
        producto=request.GET['prd']

        articulo=nuevo.objects.filter(descri__icontains=producto)
        articulos=nuevo.objects.filter(categoria__icontains=producto)

        return render(request,"./producto/buscar.html",
        {"articulos":articulos,"articulo":articulo,"query":producto})
    else:
        mensaje='No has introduccido nada'
    return render(request,'./producto/buscar.html')

@login_required
def carrito(request):
    if request.GET['prd']:
        productos=request.GET['prd']

        articulos=nuevo.objects.filter(id__icontains=productos)
        
        return render(request,'./compras/carrito.html',{'productos':productos,'articulos':articulos})

    return render(request,'./compras/carrito.html')
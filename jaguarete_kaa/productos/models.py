from django.db import models

# Create your models here.
class nuevo(models.Model):

    nombre=models.CharField(max_length=30)
    categoria=models.CharField(max_length=20)
    imagen=models.ImageField(upload_to='imagenes/')
    descri=models.CharField(max_length=1000)
    precio=models.CharField(max_length=20)

    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

    def __str__(self):

        return '{} by @{}'.format(self.nombre,self.descri)

class carrito(models.Model):
    usuario=models.CharField(max_length=30)
    lista_producto=models.CharField(max_length=30)
    total_carrito=models.CharField(max_length=30)

    def __str__(self):
        return '{} by @{}'.format(self.usuario,self.lista_producto)
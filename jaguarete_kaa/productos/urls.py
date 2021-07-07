from django.urls import path

from . import views



urlpatterns = [
    path("",views.home,name="home"),
    path("carro/", views.carrito,name="carrito"),
    path("producto/",views.producto,name="producto"),
    path("editar/",views.editar,name="editar"),
    path("crear/",views.crear,name="crear"),
    path('buscar/',views.busqueda_productos,name="buscar"),
    path('eliminar/',views.eliminar,name="eliminar"),
]
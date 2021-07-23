from django.urls import path
from .views import agregarProducto, modificarProducto, obtenerProductos
urlpatterns = [
    path('',obtenerProductos, name='listar_productos'),
    path('nuevo-producto/',agregarProducto, name='nuevo_producto'),
    path('modificar_producto/<int:idProducto>',modificarProducto, name='modificar_producto'),

]
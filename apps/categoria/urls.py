from django.urls import path
from .views import agregarCategoria, modificarCategoria, obtenerCategorias

urlpatterns = [
    path('',obtenerCategorias, name='listar_categorias'),
    path('nueva-categoria/', agregarCategoria, name='nueva_categoria'),
    path('modificar-categoria/<int:idCategoria>',modificarCategoria , name='modificar_categoria')

]
from django.urls import path
from .views import obtenerproducto, buscarproductoid, nuevoproducto, modificarproductoid

urlpatterns = [
    path('',obtenerproducto, name='listarproducto'),
    path('<int:id>/', buscarproductoid, name='buscarproducid'),
    path('nuevo/', nuevoproducto, name='nueva'),
    path('modificar/<int:id>/', modificarproductoid, name='modificar'),

]
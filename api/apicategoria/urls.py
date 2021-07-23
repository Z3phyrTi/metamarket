from django.urls import path
from .views import nuevacategoria, obtenercategorias, buscarcategoriaid, modificarcategoriaid

urlpatterns = [
    path('',obtenercategorias, name='listar'),
    path('<int:id>/', buscarcategoriaid, name='buscarporid'),
    path('nuevo/', nuevacategoria, name='nueva'),
    path('modificar/<int:id>/', modificarcategoriaid, name='modificar'),

]
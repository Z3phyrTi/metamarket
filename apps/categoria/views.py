from .models import Categoria
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import FormularioCategoria
from django.contrib.auth.decorators import login_required
# Create your views here
@login_required
def obtenerCategorias(request):
    categorias = Categoria.objects.all()
    contexto = {
        'categorias': categorias
    }
    return render(
        request,
        'categoria/index.html',
        context = contexto
    )
@login_required
def agregarCategoria(request):
    formulario = None
    if request.method == 'GET':
        formulario = FormularioCategoria()
    elif request.method == 'POST':
        formulario = FormularioCategoria(request.POST)
        formulario.save()
        return redirect('listar_categorias')
    contexto = {
        'formulario': formulario
    }
    return render(
        request,
        'categoria/nuevo.html',
        context= contexto
    )
@login_required    
def modificarCategoria(request, idCategoria):
    categoria = None
    try:
        categoria = Categoria.objects.get(pk = idCategoria)
    except ObjectDoesNotExist as e:
        pass
    if categoria == None:
        return redirect('listar_categoria')
    formulario = None
    if request.method == 'GET':
        formulario = FormularioCategoria(instance = categoria)
    if request.method == 'POST':
        formulario = FormularioCategoria(data = request.POST, instance = categoria)
        if formulario.is_valid():
            formulario.save()
            return redirect('listar_categorias')
        else:
            formulario = FormularioCategoria(instance = categoria)
    contexto ={
        'ruta':'categoria',
        'formulario': formulario
    }
    return render(request,'categoria/modificar.html', context=contexto)
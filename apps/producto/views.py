from django.shortcuts import render, redirect
from .models import Producto
from .forms import FormularioProducto
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

# Create your views here.
def obtenerProductos(request):
    productos = Producto.objects.all()
    contexto = {
        'ruta':'producto',
        'productos':productos
    }
    return render(
        request,
        'producto/index.html',
        context = contexto
    )
@login_required
def agregarProducto(request):
    formulario = None
    if request.method == 'GET': 
        formulario = FormularioProducto()
    elif request.method == 'POST':
        formulario = FormularioProducto(request.POST,request.FILES)
        formulario.save()
        return redirect('listar_productos')
    contexto = {
        'ruta':'producto',
        "formulario": formulario
    }
    return render(
        request,
        'producto/nuevo.html',
        context = contexto
    )
@login_required
def modificarProducto(request, idProducto):
    producto = None
    try:
        producto = Producto.objects.get(pk= idProducto)
    except ObjectDoesNotExist as e:
        pass
    if producto == None:
        return redirect('listar_productos')
    formulario = None
    if request.method == 'GET':
        formulario = FormularioProducto(instance = producto)
    if request.method == 'POST':
        formulario = FormularioProducto(request.POST, request.FILES, instance = producto)
        if formulario.is_valid():
            formulario.save()
            return redirect('listar_productos')
        else:
            formulario = FormularioProducto(instance = producto)
    contexto = {
        'ruta':'producto',
                'formulario': formulario
            }
    return render(request,'producto/modificar.html',context=contexto)
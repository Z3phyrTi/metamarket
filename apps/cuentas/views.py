from apps.cuentas.forms import RegistroUsuario, IniciarSesion
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
# poner refresh date base
# Create your views here.
def registro(request):
    formulario = None
    if request.method =='POST':
        formulario = RegistroUsuario(request.POST)
        if formulario.is_valid():
            usuario = formulario.save()
            usuario.refresh_from_db()
            usuario.save()
            return redirect('principal')
    if request.method == 'GET':
        formulario = RegistroUsuario()
    contexto = {
        'formulario':formulario
    }
    return render(request,'cuenta/registro.html', context = contexto)


def salir(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('principal')

def iniciarSesion(request):
    formulario = None
    if request.method == 'GET':
        formulario = IniciarSesion(request)
    if request.method == 'POST':
        usuario = request.POST['username']
        contrasena = request.POST['password']
        usuario = authenticate(username=usuario, password = contrasena)
        if usuario is not None:
            login(request, usuario)
            return redirect('principal')
        
    contexto = {
        'formulario': formulario
    }
    return render(request, 'cuenta/acceder2.html',context= contexto)
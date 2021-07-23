from apps.cuentas.forms import IniciarSesion
from django.urls import path
from django.utils import html
from .views import registro, salir, iniciarSesion
from django.contrib.auth.views import LoginView
urlpatterns = [
    path('registro/',registro, name='registro'),
    path('salir/', salir, name='salir'),
    path('iniciar-sesion/', iniciarSesion, name='iniciar_sesion')
]
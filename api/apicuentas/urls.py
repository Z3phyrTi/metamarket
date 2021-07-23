from django.urls import path
from rest_framework.decorators import api_view
from.views import iniciarSesion

urlpatterns =[
    path('iniciar/', iniciarSesion, name='iniciarSesion')
]
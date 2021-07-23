from django.http import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
# Create your views here
@api_view(['POST'])
def iniciarSesion(request):
    if request.user.is_authenticated:
        return Response(data= {'mensaje':'usuario logeado'}, status=403)
    username = request.data['username']
    password = request.data['password']
    usuariologeado = authenticate(username = username, password=password)
    if usuariologeado is not None:
        respuesta = {}
        token = ''
        try:
            token = Token.objects.get(user_id=usuariologeado.id)
        except Token.DoesNotExist:
            token = Token.objects.create(user= usuariologeado)

        respuesta['token'] = token.key
        return Response(data = respuesta, status=200)
    return Response(data= request.data, status=200)
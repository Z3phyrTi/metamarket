from rest_framework.response import Response
from apps.producto.models import Producto
from .serializers import productoserializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def obtenerproducto(request):
    producto = Producto.objects.all()
    categoriasSerializacion = productoserializer(producto, many =True)
    return Response(categoriasSerializacion.data, 200)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def buscarproductoid(id):
    producto = None
    try:
        producto = Producto.objects.get(pk = id)
    except ObjectDoesNotExist: 
        return Response(data = None,status=404)
    respuesta = buscarproductoid(producto,many= False)
    return Response(respuesta.data, 200)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def nuevoproducto(request):
    productoserializado = productoserializer(data = request.data)
    if productoserializado.is_valid():
        respuesta = productoserializado.save()
        productoserializado = productoserializer(respuesta, many = False)
        return Response(data = productoserializado, status= 201)
    return Response(data = None, status=403)


@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def modificarproductoid(request, id):
    productoecontrada = Producto.objects.get(pk = id)
    if productoecontrada == None:
        return Response(data = None, status=404)
    productoserializado = productoserializer(instance = productoecontrada, data = request.data)
    if productoserializado.is_valid():
        modificacion = productoserializado.save()
        return Response(data = modificacion, status= 200)
    return Response(data = None, status=403)
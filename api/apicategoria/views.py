from rest_framework.response import Response
from apps.categoria.models import Categoria
from .serializers import categoriaserializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def obtenercategorias(request):
    categoria = Categoria.objects.all()
    categoriasSerializacion = categoriaserializer(categoria, many =True)
    return Response(categoriasSerializacion.data, 200)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def buscarcategoriaid(id):
    categoria = None
    try:
        categoria = Categoria.objects.get(pk = id)
    except ObjectDoesNotExist: 
        return Response(data = None,status=404)
    respuesta = buscarcategoriaid(categoria,many= False)
    return Response(respuesta.data, 200)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def nuevacategoria(request):
    categoriaserializada = categoriaserializer(data = request.data)
    if categoriaserializada.is_valid():
        respuesta = categoriaserializada.save()
        categoriaserializada = categoriaserializer(respuesta, many = False)
        return Response(data = categoriaserializada.data, status= 201)
    return Response(data = None, status=403)
    
@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def modificarcategoriaid(request, id):
    categoriaencontrada = Categoria.objects.get(pk = id)
    if categoriaencontrada == None:
        return Response(data = None, status=404)
    categoriaserizada = categoriaserializer(instance = categoriaencontrada, data = request.data)
    if categoriaserizada.is_valid():
        modificacion = categoriaserizada.save()
        return Response(data = modificacion, status= 200)
    return Response(data = None, status=403)
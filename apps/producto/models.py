from django.db import models
from apps.categoria.models import Categoria
from os.path import join
# Create your models here.
def cambiar_nombre(instance, filename):
    extension = filename.split('.')[-1]
    filename = "{}_{}.{}".format(
        instance.nombre_producto,
        instance.codigo_barra,
        extension
    )
    return join('productos',filename)
class Producto(models.Model):
    imagen = models.ImageField('Imagen del producto', upload_to='productos',blank= True, null= False)
    nombre_producto = models.CharField('Nombre del producto', max_length=50, blank= False, null= False)
    caracteristicas_producto = models.CharField('Caracteristicas del producto',  max_length=50, blank= False, null= False)
    precio_producto = models.SmallIntegerField('Precio del producto', blank=False, null= False)
    codigo_barras = models.CharField('Codigo de barras', max_length=150, blank=False, null= False)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null= True)
    def __str__(self):
        return self.nombre_producto
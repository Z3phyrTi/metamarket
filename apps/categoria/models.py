from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre_categoria = models.CharField(' Nombre de la categoria ', max_length=50,blank= False, null= False)
    descripcion_categoria = models.CharField(' Descripcion de la categoria ',max_length=150,blank= False, null= False)
    def __str__(self):
        return self.nombre_categoria
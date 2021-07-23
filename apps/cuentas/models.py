
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.
class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario.username
@receiver(post_save, sender=User)
def actualizar_perfil(sender, instance, created, *args, **kwargs):
    if created:
        Perfil.objects.create(usuario = instance)
    instance.perfil.save()
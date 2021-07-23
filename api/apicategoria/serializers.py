from django.db.models.base import Model
from apps.categoria.models import Categoria
from rest_framework import  serializers

class categoriaserializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
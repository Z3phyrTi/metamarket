from apps.producto.models import Producto
from rest_framework import  serializers

class productoserializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'
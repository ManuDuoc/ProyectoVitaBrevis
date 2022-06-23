from rest_framework import serializers
from core.models import Producto
class ProductoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

    nombreCategoria = serializers.CharField(read_only=True, source="categoria.nombreCategoria")
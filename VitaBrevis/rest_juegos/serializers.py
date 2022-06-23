from rest_framework import serializers
from core.models import Producto,Categoria
from django.contrib.auth.models import User

class ProductoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

    nombreCategoria = serializers.CharField(read_only=True, source="categoria.nombreCategoria")



class CategoriaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields =['codigo','nombreCategoria']

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


from rest_framework import serializers
from core.models import Categoria
class CategoriaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields =['codigo','nombreCategoria']
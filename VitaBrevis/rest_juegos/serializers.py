from rest_framework import serializers
from core.models import Producto
class ProductoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields =['codigo','nombre','precio','video','foto','descripcion','stock','masInfo1' ,'masInfo2' ,'masInfo3' ,'masInfo4' ,'masInfo5' ,'categoria']
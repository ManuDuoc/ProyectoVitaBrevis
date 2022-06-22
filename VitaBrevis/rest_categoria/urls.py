from django.urls import path
from rest_categoria.views import lista_categorias,detalle_categoria

urlpatterns = [
    path('lista_categorias', lista_categorias , name="lista_categorias"),
    path('detalle_categoria/<codigo>', detalle_categoria , name ="detalle_categoria"),
]
from django.urls import path
from rest_juegos.views import lista_juegos,detalle_juego,lista_categorias,detalle_categoria,lista_usuarios,detalle_usuario
from rest_juegos.viewsLogin import loginApi

urlpatterns = [
    path('lista_juegos', lista_juegos , name="lista_juegos"),
    path('detalle_juego/<codigo>', detalle_juego , name ="detalle_juego"),
    path('loginApi/',loginApi,name="loginApi"),
    path('lista_categorias', lista_categorias , name="lista_categorias"),
    path('detalle_categoria/<codigo>', detalle_categoria , name ="detalle_categoria"),
    path('lista_usuarios', lista_usuarios , name="lista_usuarios"),
    path('detalle_usuario/<id>', detalle_usuario , name ="detalle_usuario"),
]
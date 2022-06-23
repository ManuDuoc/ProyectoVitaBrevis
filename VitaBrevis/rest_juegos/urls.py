from django.urls import path
from rest_juegos.views import lista_juegos,detalle_juego
from rest_juegos.viewsLogin import loginApi

urlpatterns = [
    path('lista_juegos', lista_juegos , name="lista_juegos"),
    path('detalle_juego/<codigo>', detalle_juego , name ="detalle_juego"),
    path('loginApi/',loginApi,name="loginApi"),
]
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import inicio, PS5, registro, login, administrador,anadirjuego,listajuegos,registrarjuego,eliminarJuego,edicionJuegos,editarjuego,inicios,Juego,Categorias

urlpatterns = [
    path('', inicio,name="Principal"),
    path('PS5', PS5,name="PS5"),
    path('registro', registro,name="registro"),
    path('login', login,name="login"),
    path('administrador',administrador,name='administrador'),
    path('anadirjuego',anadirjuego,name='anadirjuego'),
    path('listajuegos',listajuegos,name='listajuegos'),
    path('registrarjuego/',registrarjuego,name='registrarjuego'),
    path('eliminarJuego/<codigo>',eliminarJuego,name='eliminarJuego'),
    path('edicionJuegos/<codigo>',edicionJuegos,name='edicionJuegos'),
    path('editarjuego/',editarjuego,name='editarjuego'),
    path('inicio',inicios,name="inicio"),
    path('Juegos/<codigo>',Juego,name='Juego'),
    path('Categoria/<nombreCategoria>',Categorias,name='Juego')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
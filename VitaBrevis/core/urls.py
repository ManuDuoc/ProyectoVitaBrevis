from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import inicio, PS5, accion, deporte, simulacion, terror, registro, login, juego,administrador,anadirjuego,listajuegos,registrarjuego

urlpatterns = [
    path('', inicio,name="Principal"),
    path('PS5', PS5,name="PS5"),
    path('accion', accion,name="accion"),
    path('deporte', deporte,name="deporte"),
    path('simulacion', simulacion,name="simulacion"),
    path('terror', terror,name="terror"),
    path('registro', registro,name="registro"),
    path('login', login,name="login"),
    path('juego', juego,name="juego"),
    path('administrador',administrador,name='administrador'),
    path('anadirjuego',anadirjuego,name='anadirjuego'),
    path('listajuegos',listajuegos,name='listajuegos'),
    path('registrarjuego/',registrarjuego,name='registrarjuego'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
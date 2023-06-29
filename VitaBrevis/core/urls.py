from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from .views import inicio, registrarPerfil, usuario, registro, administrador,anadirjuego,listajuegos,registrarjuego,eliminarJuego,edicionJuegos,editarjuego,inicios,Juego,Categorias,Usuarios,eliminarUsuario,anadirPerfil,registrarPerfil,edicionPerfil,editarPerfil,compra

urlpatterns = [
    path('', inicio,name="Principal"),
    path('usuario', usuario,name="usuario"),
    path('administrador',administrador,name='administrador'),
    path('anadirjuego',anadirjuego,name='anadirjuego'),
    path('listajuegos',listajuegos,name='listajuegos'),
    path('registrarjuego/',registrarjuego,name='registrarjuego'),
    path('registrarPerfil/',registrarPerfil,name='registrarPerfil'),
    path('eliminarJuego/<codigo>',eliminarJuego,name='eliminarJuego'),
    path('edicionJuegos/<codigo>',edicionJuegos,name='edicionJuegos'),
    path('editarjuego/',editarjuego,name='editarjuego'),
    path('editarPerf/',editarPerfil,name='editarPerfil'),
    path('inicio',inicios,name="inicio"),
    path('Juegos/<codigo>',Juego,name='Juego'),
    path('Categoria/<nombreCategoria>',Categorias,name='Juego'),
    path('listaUsuarios',Usuarios,name='listaUsuarios'),
    path('eliminarUsuario/<id>',eliminarUsuario,name='eliminarUsuario'),
    path('anadirPerfil',anadirPerfil,name='anadirPerfil'),
    path('editarPerfil',edicionPerfil,name='edicionPerfil'),
    path('compra',compra,name='compra'),


    path('registro', registro,name="registro"),
    path('login/', LoginView.as_view(template_name='core/login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='core/logout.html'), name="logout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path
from rest_juegos.views import lista_juegos

urlpatterns = [
    path('lista_juegos', lista_juegos , name="lista_juegos"),
]
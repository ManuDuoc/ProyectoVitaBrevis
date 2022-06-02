from django.contrib import admin
from .models import Categoria,Juego
from .models import Producto


# Register your models here.
admin.site.register(Categoria)
admin.site.register(Juego)
admin.site.register(Producto)
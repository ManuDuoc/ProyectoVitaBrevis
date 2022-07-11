from django.contrib import admin
from .models import Categoria
from .models import Producto,Perfil


# Register your models here.
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Perfil)
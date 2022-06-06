from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Categoria(models.Model):
    codigo = models.IntegerField(primary_key=True, verbose_name='Codigo de la Categoria')
    nombreCategoria = models.CharField(max_length=20, verbose_name='Categoria', blank=False, null=False)

    def __str__(self):
        return self.nombreCategoria


class Producto(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    precio = models.PositiveSmallIntegerField()
    video = models.CharField(max_length=150,null=True)
    foto = models.ImageField(upload_to="juegos", null= True)
    descripcion = models.TextField(null=True)
    stock = models.PositiveSmallIntegerField(null=True)
    masInfo1 = models.TextField(blank=True,null=True,verbose_name = 'Mas Informacion del Juego 1')
    masInfo2 = models.TextField(blank=True,null=True,verbose_name = 'Mas Informacion del Juego 2')
    masInfo3 = models.TextField(blank=True,null=True,verbose_name = 'Mas Informacion del Juego 3')
    masInfo4 = models.TextField(blank=True,null=True,verbose_name = 'Mas Informacion del Juego 4')
    masInfo5 = models.TextField(blank=True,null=True,verbose_name = 'Mas Informacion del Juego 5')
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE,null=True)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.codigo)
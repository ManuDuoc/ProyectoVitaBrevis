# Generated by Django 4.0.4 on 2022-06-04 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_rename_imagen_producto_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='juego',
            name='foto',
        ),
    ]

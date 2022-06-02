# Generated by Django 4.0.4 on 2022-06-01 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_producto_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='masInfo1',
            field=models.TextField(null=True, verbose_name='Mas Informacion del Juego 1'),
        ),
        migrations.AddField(
            model_name='producto',
            name='masInfo2',
            field=models.TextField(null=True, verbose_name='Mas Informacion del Juego 2'),
        ),
        migrations.AddField(
            model_name='producto',
            name='masInfo3',
            field=models.TextField(null=True, verbose_name='Mas Informacion del Juego 3'),
        ),
        migrations.AddField(
            model_name='producto',
            name='masInfo4',
            field=models.TextField(null=True, verbose_name='Mas Informacion del Juego 4'),
        ),
        migrations.AddField(
            model_name='producto',
            name='masInfo5',
            field=models.TextField(null=True, verbose_name='Mas Informacion del Juego 5'),
        ),
    ]

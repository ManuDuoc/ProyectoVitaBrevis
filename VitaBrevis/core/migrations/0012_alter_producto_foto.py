# Generated by Django 4.0.4 on 2022-06-23 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_producto_stock_delete_juego'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='juegos'),
        ),
    ]

# Generated by Django 4.0.4 on 2022-07-11 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_perfil_apellido_perfil_edad_perfil_estado_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='juego',
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='masinfo',
        ),
    ]
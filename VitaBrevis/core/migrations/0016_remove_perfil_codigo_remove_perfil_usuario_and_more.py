# Generated by Django 4.0.4 on 2022-07-11 00:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0015_remove_perfil_id_perfil_codigo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='codigo',
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='usuario',
        ),
        migrations.AddField(
            model_name='perfil',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
    ]

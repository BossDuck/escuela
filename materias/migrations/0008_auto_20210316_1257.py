# Generated by Django 3.1.6 on 2021-03-16 18:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('materias', '0007_materia_maestro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materia',
            name='maestro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Maestro'),
        ),
    ]

# Generated by Django 3.1.6 on 2021-03-13 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maestros', '0002_grupo_enrolado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupo',
            name='nombre',
            field=models.CharField(max_length=10, unique=True, verbose_name='Nombre del Grupo'),
        ),
    ]
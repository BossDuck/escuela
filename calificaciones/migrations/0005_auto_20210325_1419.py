# Generated by Django 3.1.6 on 2021-03-25 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('materias', '0008_auto_20210316_1257'),
        ('calificaciones', '0004_calificacion_periodo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calificacion',
            name='materia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='materias.materia', verbose_name='Materia'),
        ),
    ]

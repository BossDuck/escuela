# Generated by Django 3.1.6 on 2021-03-25 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calificaciones', '0002_calificacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calificacion',
            name='bloque1',
            field=models.FloatField(blank=True, null=True, verbose_name='Bloque 1'),
        ),
        migrations.AlterField(
            model_name='calificacion',
            name='bloque2',
            field=models.FloatField(blank=True, null=True, verbose_name='Bloque 1'),
        ),
        migrations.AlterField(
            model_name='calificacion',
            name='bloque3',
            field=models.FloatField(blank=True, null=True, verbose_name='Bloque 1'),
        ),
        migrations.AlterField(
            model_name='calificacion',
            name='semestral',
            field=models.FloatField(blank=True, null=True, verbose_name='Semestral'),
        ),
    ]

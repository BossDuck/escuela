# Generated by Django 3.1.6 on 2021-03-18 01:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maestros', '0005_auto_20210316_1308'),
        ('user', '0007_user_grupo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='grupo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='maestros.grupo', verbose_name='Grupo'),
        ),
    ]

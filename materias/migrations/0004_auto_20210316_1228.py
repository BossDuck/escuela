# Generated by Django 3.1.6 on 2021-03-16 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materias', '0003_materia_maestro'),
    ]

    operations = [
        migrations.RenameField(
            model_name='materia',
            old_name='maestro',
            new_name='user',
        ),
    ]
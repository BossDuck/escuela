from django.db import models
from django.contrib.auth.models import AbstractUser
from maestros.models import Grupo

# Create your models here.


class User(AbstractUser):
    maestro='maestro'
    
    TIPO_CHOICES = [
        ('maestro', 'Maestro'),
        ('alumno', 'Alumno'),
        ('padre', 'Padre'),
        ('admin', 'Admin')
    ]

    imagen=models.ImageField(default="null", upload_to="users/", verbose_name="Imagen del Usuario")
    tipoUsuario=models.CharField(max_length=10, default=maestro, choices=TIPO_CHOICES, verbose_name="Tipo de Usuario")
    grupo=models.ForeignKey(Grupo, on_delete=models.CASCADE, verbose_name="Grupo",default=1)
    curp=models.CharField(max_length=18, verbose_name="CURP", null=True, blank=True)
    telefono=models.CharField(max_length=10, verbose_name="Teléfono", null=True, blank=True)
    padre=models.CharField(max_length=100, verbose_name="Padre", null=True, blank=True)
    madre=models.CharField(max_length=100, verbose_name="Madre", null=True, blank=True)
    direccion=models.CharField(max_length=200, verbose_name="Dirección", null=True, blank=True)
    padecimientos=models.TextField(verbose_name="Padecimientos", default="")

   


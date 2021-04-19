from django.db import models
#from user.models import User
# Create your models here.

class Grupo(models.Model):

    nombre=models.CharField(unique=True,max_length=10, verbose_name="Nombre del Grupo")
    class Meta:
        verbose_name="Grupo"
        verbose_name_plural="Grupos"

    def __str__(self):
        return self.nombre
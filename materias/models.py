from django.db import models
from maestros.models import Grupo
from user.models import User

# Create your models here.

class Materia(models.Model):

    nombre=models.CharField(max_length=50, verbose_name="Nombre")
    grupo=models.ForeignKey(Grupo, verbose_name="Grupo", on_delete=models.CASCADE)
    maestro=models.ForeignKey(User, verbose_name="Maestro", on_delete=models.CASCADE)

    class Meta:
        verbose_name="Materia"
        verbose_name_plural="Materias"

    def __str__(self):
        return self.nombre
    
from django.db import models
from user.models import User
from materias.models import Materia
# Create your models here.

class Periodo(models.Model):

    nombre=models.CharField(max_length=50, verbose_name="Nombre")
    inicio=models.DateTimeField(auto_now=False, verbose_name="Inicio")
    fin=models.DateTimeField(auto_now=False, verbose_name="Fin")

    class Meta:
        verbose_name="Periodo"
        verbose_name_plural="Periodos"
    
    def __str__(self):
        return self.nombre

class Calificacion(models.Model):
    alumno=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Alumno")
    materia=models.ForeignKey(Materia, on_delete=models.CASCADE, verbose_name="Materia",blank=True, null=True)
    periodo=models.ForeignKey(Periodo, on_delete=models.CASCADE, verbose_name="Periodo",blank=True, null=True)
    bloque1=models.FloatField(verbose_name="Bloque 1", blank=True, null=True)
    bloque2=models.FloatField(verbose_name="Bloque 1", blank=True, null=True)
    bloque3=models.FloatField(verbose_name="Bloque 1", blank=True, null=True)
    semestral=models.FloatField(verbose_name="Semestral", blank=True, null=True)
    


    
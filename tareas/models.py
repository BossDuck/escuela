from django.db import models
from ckeditor.fields import RichTextField
from user.models import User
from materias.models import Materia
# Create your models here.

class Tarea(models.Model):

    titulo=models.CharField(max_length=100, verbose_name="Titulo")
    descripcion=models.CharField(max_length=100, verbose_name="Descripcion")
    contenido=RichTextField(verbose_name="Contenido")
    documento=models.FileField(upload_to="documentos/", default="null")
    fecha_entrega=models.DateTimeField(auto_now=False, verbose_name="Fecha de entrega")
    #user=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Maestro")
    materia=models.ForeignKey(Materia, on_delete=models.CASCADE, verbose_name="Materia", default="")

    class Meta:
        verbose_name="Tarea"
        verbose_name_plural="Tareas"

    def __str__(self):
        return self.titulo
    
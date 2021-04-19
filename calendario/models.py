from django.db import models

# Create your models here.

class EventoCalendario(models.Model):
    
    titulo=models.CharField(max_length=50, verbose_name="Titulo")
    descripcion=models.TextField(verbose_name="Descripción", default="")
    fecha_evento=models.DateTimeField(auto_now=False, verbose_name="Fecha")
    tipo_evento=models.CharField(max_length=10, verbose_name="Tipo")
    class Meta:
        verbose_name="Evento"
        verbose_name_plural="Eventos"

    def __str__(self):
        return self.titulo
    
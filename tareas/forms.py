from django import forms
from django.forms import ModelForm
from tareas.models import Tarea

class TareaForm(ModelForm):

    class Meta:
        model=Tarea
        fields='__all__'
        
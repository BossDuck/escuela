from django import forms
from materias.models import Materia
from django.forms import ModelForm

class MateriaForm(ModelForm):
    class Meta:
        model = Materia
        fields='__all__'
        
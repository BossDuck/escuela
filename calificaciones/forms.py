from django import forms
from django.forms import ModelForm
from calificaciones.models import Periodo
class PeriodoForm(ModelForm):

    class Meta:
        model=Periodo
        fields='__all__'
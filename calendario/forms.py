from django import forms
from django.forms import ModelForm
from calendario.models import EventoCalendario
class EventoForm(ModelForm):

    class Meta:
        model=EventoCalendario
        fields='__all__'
        
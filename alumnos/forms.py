from django import forms
from django.forms import ModelForm
from user.models import User
from django.contrib.auth.forms import UserCreationForm


class AlumnoForm(UserCreationForm):
    
    class Meta:
        model=User
        
        fields=['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'imagen', 'tipoUsuario', 'grupo','curp','telefono','padre','madre','direccion','padecimientos']
        

        
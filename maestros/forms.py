from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from user.models import User
from maestros.models import Grupo


class MaestroFormm(UserCreationForm):

    class Meta:
        model=User
        fields=['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'imagen', 'tipoUsuario', 'grupo', 'curp', 'telefono', 'direccion', 'padecimientos' ]
    

class GrupoForm(ModelForm):

    class Meta:
        model=Grupo
        fields='__all__'
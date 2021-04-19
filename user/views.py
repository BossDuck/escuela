from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from calendario.models import EventoCalendario
from user.models import User
from materias.models import Materia
from tareas.models import Tarea

# Create your views here.
@login_required(login_url='login')
def inicio(request):
    eventos=EventoCalendario.objects.all()
    return render(request,'inicio.html',{
        'eventos':eventos
    })

def usuariosLogin(request):

    if request.user.is_authenticated:
        return redirect('inicio')
    else:
        if request.method=='POST':
            username=request.POST.get('email')
            password=request.POST.get('password')

            user=authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('inicio')
            else:
                messages.warning(request, "Email o Contraseña incorrectos")
                return redirect('login')

    return render(request, 'login.html')

def usuariosLogout(request):
    logout(request)
    return redirect('login')







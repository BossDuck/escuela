from django.shortcuts import render, redirect
from maestros.forms import MaestroFormm, GrupoForm
from django.contrib import messages
from user.models import User
from maestros.models import Grupo

# Create your views here.

def mostrarMaestros(request):
    if request.user.tipoUsuario != 'admin':
        messages.warning(request, "Permisos de Administrador Requeridos")
        return redirect('inicio')
    else:
        maestros=User.objects.filter(tipoUsuario="Maestro")

    return render(request, 'lista-maestros.html',{
       'maestros': maestros
    })

def crearMaestro(request):
    
    if request.user.tipoUsuario != 'admin':
        return redirect('inicio')
    else:
        maestroForm=MaestroFormm()

        if request.method=='POST':
            try:
                maestroForm=MaestroFormm(request.POST, request.FILES)

                if maestroForm.is_valid():
                    maestroForm.save()
                    messages.success(request,"Guardado Correctamente")
                    return redirect('añadir-maestro')
            except:
                messages.warning(request, "Error al Guardar")
                return redirect('añadir-maestro')

    return render(request, 'crear-maestro.html', {
        'form':maestroForm
    })

def eliminarMaestro(request,id):
    if request.user.tipoUsuario != 'admin':
        messages.warning(request, "Permisos de Administrador Requeridos")
        return redirect('inicio')
    else:
        try:
            maestro=User.objects.get(id=id)
            maestro.delete()
            messages.success(request,"Eliminado Correctamente")
            return redirect('listar-maestros')
        except:
            messages.warning(request, "Error al Eliminar")
            return redirect('listar-maestros')


def editarMaestro(request, id):
    if request.user.tipoUsuario != 'admin':
        messages.warning(request, "Permisos de Administrador Requeridos")
        return redirect('inicio')
    else:
        maestro=User.objects.get(id=id)
        maestroForm=MaestroFormm()

        if request.method=='POST':
            try:
                nombre=request.POST.get('first_name')
                apellidos=request.POST.get('last_name')
                email=request.POST.get('email')
                username=request.POST.get('username')
                User.objects.filter(id=id).update(first_name=nombre ,last_name=apellidos,email=email, username=username)
                messages.success(request, "Actualizado Correctamente")
                return redirect('listar-maestros')
            except:
                messages.warning(request, "Error al Editar")
                return redirect('listar-maestros')

    return render(request, 'editar-maestro.html',{
        'maestro':maestro,
        'form' : maestroForm
    })

def mostrarGrupos(request):
    if request.user.tipoUsuario != 'admin':
        messages.warning(request, "Permisos de Administrador Requeridos")
        return redirect('inicio')
    else:
        grupos=Grupo.objects.all()

    return render(request, 'listar-grupos.html',
    {
        'grupos':grupos
    })
def crearGrupo(request):

    if request.user.tipoUsuario != 'admin':
        messages.warning(request, "Permisos de Administrador Requeridos")
        return redirect('inicio')
    else:
        maestros=User.objects.filter(tipoUsuario='maestro')
        if request.method=='POST':
            try:
                nombre=request.POST.get('nombre')
                #enrolado=int(request.POST.get('teachers'))
                enrolar=Grupo(
                    nombre=nombre
                    #enrolado_id=enrolado
                )
                enrolar.save()
                messages.success(request, "Guardado Correctamente")
                return redirect('añadir-grupo')
            except:
                messages.warning(request,'Error al Guardar')
                return redirect('añadir-grupo')


            
    return render(request, 'crear-grupo.html',
    {
        'maestros':maestros
    })

def eliminarGrupo(request, id):
    if request.user.tipoUsuario!='admin':
        messages.warning(request, "Permisos de Administrador Requeridos")
        return redirect('inicio')
    else:
        try:
            grupo=Grupo.objects.get(id=id)
            grupo.delete()
            messages.success(request, 'Eliminado Correctamente')
            return redirect('listar-grupos')
        except:
            messages.warning(request, "Error al Eliminar")
            return redirect('listar-grupos')

def editarGrupo(request, id):
    if request.user.tipoUsuario != 'admin':
        messages.warning(request, "Permisos de Administrador Requeridos")
        return redirect('inicio')
    else:
        grupo=Grupo.objects.get(id=id)
        maestros=User.objects.filter(tipoUsuario='maestro')
        if request.method == 'POST':
            try:
                nombre=request.POST.get('nombre')
                #maestro=int(request.POST.get('teachers'))
                Grupo.objects.filter(id=id).update(nombre=nombre)
                messages.success(request, "Actualizado Correctamente")
                return redirect('listar-grupos')
            except:
                messages.warning(request, "Error al Editar")
                return redirect('listar-grupos')

    return render(request, 'editar-grupo.html', {
        'grupo':grupo,
        'maestros': maestros
    })
    
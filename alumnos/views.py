from django.shortcuts import render, redirect
from user.models import User
from alumnos.forms import AlumnoForm
from django.contrib import messages
from maestros.models import Grupo

# Create your views here.

def crearAlumno(request):
    if request.user.tipoUsuario != 'admin':
        messages.warning(request, "Permisos de Administrador Requeridos")
        return redirect('inicio')
    else:
        alumnoForm=AlumnoForm()
        if request.method=='POST':
            try:
                alumnoForm=AlumnoForm(request.POST, request.FILES)
                if alumnoForm.is_valid():
                    alumnoForm.save()
                    messages.success(request, "Guardado Correctamente")
                    return redirect('añadir-alumno')
            except:
                messages.warning(request, "Error al Guardar")
                return redirect('añadir-alumno')

    return render(request, 'crear-alumno.html',{
        'form':alumnoForm
    })

def mostrarAlumnos(request):

    if request.user.tipoUsuario != 'admin':
        messages.warning(request, "Permisos de Administrador Requeridos")
        return redirect('inicio')
    else:
        alumnos=User.objects.filter(tipoUsuario='alumno')


    return render(request, 'listar-alumnos.html',{
        'alumnos':alumnos
    })

def eliminarAlumno(request, id):
    if request.user.tipoUsuario != 'admin':
        messages.warning(request, "Permisos de Administrador Requeridos")
        return redirect('inicio')
    else:
        try:
            alumno=User.objects.get(id=id)
            alumno.delete()
            messages.success(request, "Eliminado Correctamente")
            return redirect('listar-alumnos')
        except:
                messages.warning(request, "Error al Eliminar")
                return redirect('listar-alumnos')

def editarAlumno(request, id):
    if request.user.tipoUsuario != 'admin':
        messages.warning(request, "Permisos de Administrador Requeridos")
        return redirect('inicio')
    else:
        alumno=User.objects.get(id=id)
        grupos=Grupo.objects.all()

        if request.method=='POST':
            try:
                email=request.POST.get('email')
                username=request.POST.get('username')
                grupo=request.POST.get('grupo')
                telefono=request.POST.get('telefono')
                direccion=request.POST.get('direccion')
                padecimientos=request.POST.get('padecimientos')
                User.objects.filter(id=id).update(email=email,username=username,grupo_id=grupo, telefono=telefono,direccion=direccion, padecimientos=padecimientos)
                messages.success(request, "Actualizado Correctamente")
                return redirect('listar-alumnos')
            except:
                messages.warning(request, "Error al Editar")
                return redirect('listar-alumnos')


    return render(request,'editar-alumno.html', {
        'alumno':alumno,
        'grupos':grupos
    })



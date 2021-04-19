from django.shortcuts import render, redirect
from maestros.models import Grupo
from materias.models import Materia
from materias.forms import MateriaForm
from django.contrib import messages
from user.models import User
# Create your views here.
def crearMateria(request):
    if request.user.tipoUsuario != 'admin':
        messages.warning(request, "Permisos de Administrador Requeridos")
        return redirect('inicio')
    else:

        grupos=Grupo.objects.all()
        maestros=User.objects.filter(tipoUsuario='maestro')
        if request.method=='POST':
            try:
                nombre=request.POST.get('nombre')
                grupo=request.POST.get('grupos')
                maestro=request.POST.get('maestro')
                crearGrupo=Materia(
                    nombre=nombre,
                    grupo_id=grupo,
                    maestro_id=maestro
                )
                crearGrupo.save()
                messages.success(request, "Guardado Correctamente")
                return redirect('añadir-materia')
            except:
                messages.warning(request,"Error al Guardar")
                return redirect('añadir-materia')

    return render(request, 'crear-materia.html',{
        'grupos': grupos,
        'maestros': maestros
    })

def mostrarMaterias(request):
    if request.user.tipoUsuario != 'admin':
        messages.warning(request, "Permisos de Administrador Requeridos")
        return redirect('inicio')
    else:
        materias=Materia.objects.all()
        
    return render(request, 'listar-materias.html',{
        'materias':materias
    })

def eliminarMateria(request, id):
    if request.user.tipoUsuario != 'admin':
        messages.warning(request, "Permisos de Administrador Requeridos")
        return redirect('inicio')
    else:
        try:
            materia=Materia.objects.get(id=id)
            materia.delete()
            messages.success(request, "Eliminado Correctamente")
            return redirect('listar-materias')
        except:
            messages.warning(request, "Error al Eliminar")
            return redirect('listar-materias')

def editarMateria(request, id):
    if request.user.tipoUsuario != 'admin':
        messages.warning(request, "Permisos de Administrador Requeridos")
        return redirect('inicio')
    else:
        materia=Materia.objects.get(id=id)
        grupos=Grupo.objects.all()
        maestros=User.objects.filter(tipoUsuario='maestro')
        if request.method=='POST':
            try:
                nombre=request.POST.get('nombre')
                grupo=request.POST.get('grupos')
                maestro=request.POST.get('maestro')
                actualizar=Materia.objects.filter(id=id).update(
                    nombre=nombre,
                    grupo_id=grupo,
                    maestro_id=maestro
                )
                messages.success(request,"Actualizado Correctamente")
                return redirect('listar-materias')
            except:
                messages.warning(request, "Error al Editar")
                return redirect('listar-materias')
            

    return render(request, 'editar-materia.html',{
        'materia': materia,
        'grupos' : grupos,
        'maestros':maestros
    })

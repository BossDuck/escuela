from django.shortcuts import render,redirect
from maestros.models import Grupo
from materias.models import Materia
from tareas.models import Tarea
from django.contrib import messages
from materias.models import Materia

# Create your views here.
def crearTarea(request):
    if request.user.tipoUsuario != 'admin' and request.user.tipoUsuario != 'maestro':
        messages.warning(request, "Permisos de Administrador Requeridos")
        return redirect('inicio')
    else:
        materias=Materia.objects.filter(maestro_id=request.user.id)

        if request.method== 'POST':
            try:
                titulo=request.POST.get('titulo')
                fecha=request.POST.get('fecha')
                descripcion=request.POST.get('descripcion')
                contenido=request.POST.get('contenido')
                materia=request.POST.get('materia')
                documento=request.FILES.get('documento')

                tarea=Tarea(
                    titulo=titulo,
                    descripcion=descripcion,
                    contenido=contenido,
                    fecha_entrega=fecha,
                    materia_id=materia,
                    documento=documento
                )
                tarea.save()
                messages.success(request, "Guardado Correctamente")
                return redirect('añadir-tarea')
            except:
                messages.warning(request, "Error al Guardar")
                return redirect('añadir-tarea')

    return render(request, 'crear-tarea.html',{
        'materias':materias
    })

def visualizarGrupos(request):
    if request.user.tipoUsuario != 'admin' and request.user.tipoUsuario !='maestro':
        messages.warning(request, "Permisos de Administrador Requeridos")
        return redirect('inicio')
    else:
        #materias=Materia.objects.filter(maestro_id=request.user.id)
        #grupos=Grupo.objects.filter(grupo=materias[0].id)
        grupos=Grupo.objects.all()
   
    
    return render(request, 'visualizar-grupos.html',{
        'grupos':grupos
    })

def visualizarGrupo(request, id):
    if request.user.tipoUsuario != 'admin' and request.user.tipoUsuario != 'alumno':
        messages.warning(request, "Permisos de Administrador Requeridos")
        return redirect('inicio')
    else:
        grupo=Grupo.objects.get(id=id)
        materias=Materia.objects.filter(grupo_id=id)
    return render(request, 'visualizar-grupo.html',
    {
        'grupo':grupo,
        'materias':materias
    })

def mostrarTareas(request, id):

    tareas=Tarea.objects.filter(materia_id=id)
    return render(request, 'materia.html',
    {
        'tareas':tareas
    })

def mostrarTarea(request, id):
    tarea=Tarea.objects.get(id=id)
    return render(request, 'tarea-descripcion.html',{
        'tarea':tarea
    })

def listarTareas(request):
    if request.user.tipoUsuario!= 'admin' and request.user.tipoUsuario !='maestro':
        messages.warning(request, "Permisos de Administrador Requeridos")
        return redirect('inicio')
    else:
        materias=Materia.objects.filter(maestro_id=request.user.id)
        tareas=Tarea.objects.all()

    return render(request, 'listar-tareas.html',{
        'tareas':tareas
    })

def eliminarTarea(request, id):
    if request.user.tipoUsuario!='admin' and request.user.tipoUsuario!='maestro':
        messages.warning(request, "Permisos de Administrador Requeridos")
        return redirect('inicio')
    else:
        try:
            tarea=Tarea.objects.get(id=id)
            tarea.delete()
            messages.success(request, "Eliminado Correctamente")
            return redirect('listar-tareas')
        except:
            messages.warning(request, "Error al Eliminar")
            return redirect('listar-tareas')

    return redirect('inicio')

def editarTarea(request, id):


    return render(request, 'editar-tarea.html')
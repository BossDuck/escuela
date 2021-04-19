from django.shortcuts import render, redirect
from calificaciones.forms import PeriodoForm
from django.contrib import messages
from calificaciones.models import Periodo, Calificacion
from user.models import User
from materias.models import Materia
from maestros.models import Grupo
# Create your views here.

def crearPeriodo(request):
    if request.user.tipoUsuario != 'admin':
        messages.warning(request, "Permisos de Administrador Requeridos")
        return redirect('inicio')
    else:
        if request.method=='POST':
            try:
                nombre=request.POST.get('nombre')
                inicio=request.POST.get('inicio')
                fin=request.POST.get('fin')
                periodo=Periodo(
                    nombre=nombre,
                    inicio=inicio,
                    fin=fin
                )
                periodo.save()
                messages.success(request, "Guardado Correctamente")
                return redirect('añadir-periodo')
            except:
                messages.warning(request, "Error al Guardar")
                return redirect('añadir-periodo')

    return render(request,'añadir-periodo.html',{
        
    })

def mostrarPeriodos(request):
    if request.user.tipoUsuario!='admin':
        messages.warning(request, "Permisos de Administrador Requeridos")
        return redirect('inicio')
    else:
        periodos=Periodo.objects.all()

    return render(request, 'listar-periodo.html',{
        'periodos':periodos
    })

def eliminarPeriodo(request,id):
    if request.user.tipoUsuario!='admin':
        messages.warning(request, "Permisos de Administrador Requeridos")
        return redirect('inicio')
    else:
        try:
            periodo=Periodo.objects.get(id=id)
            periodo.delete()
            messages.success(request, "Eliminado Correctamente")
            return redirect('listar-periodos')
        except:
            messages.warning(request, "Error al Eliminar")
            return redirect('listar-periodos')

def editarPeriodo(request, id):
    if request.user.tipoUsuario!='admin':
        messages.warning(request, "Permisos de Administrador Requeridos")
        return redirect('inicio')
    else:
        periodo=Periodo.objects.get(id=id)
        if request.method=='POST':
            try:
                nombre=request.POST.get('nombre')
                inicio=request.POST.get('inicio')
                fin=request.POST.get('fin')
                periodo=Periodo.objects.filter(id=id).update(
                    nombre=nombre,inicio=inicio,fin=fin
                )
                messages.success(request, "Actualizado Correctamente")
                return redirect('listar-periodos')
            except:
                messages.warning(request, "Error al Actualizar")
                return redirect('listar-periodos')

    return render(request, 'editar-periodo.html',{
        'periodo':periodo
    })

def calificarAlumno(request, id):
    if request.user.tipoUsuario!='admin' and request.user.tipoUsuario != 'maestro':
        messages.warning(request, "Permisos de Administrador Requeridos")
        return redirect('inicio')
    else:
        alumno=User.objects.get(id=id)
        periodos=Periodo.objects.all().order_by('id')
        grupo=Grupo.objects.get(id=alumno.grupo.id)
        materias=Materia.objects.filter(grupo=grupo.id)
        
        
        if request.method=='POST':
            try:
                bloque1=request.POST.get('bloque1')
                bloque2=request.POST.get('bloque2')
                bloque3=request.POST.get('bloque3')
                semestral=request.POST.get('semestral')
                periodo=request.POST.get('periodo')
                materia=request.POST.get('materia')

                guardar=Calificacion(
                    alumno=alumno,
                    bloque1=bloque1,
                    bloque2=bloque2,
                    bloque3=bloque3,
                    semestral=semestral,
                    periodo_id=periodo,
                    materia_id=materia
                )
                guardar.save()
                messages.success(request, "Calificado Correctamente")
                return redirect('listar-alumnos')
            except:
                messages.warning(request, "Error al Calificar")
                return redirect('listar-alumnos')


    
    return render(request, 'calificar-alumno.html',{
        'alumno':alumno,
        'periodos':periodos,
        'materias':materias
    })


def boleta(request):
    if request.user.tipoUsuario != 'admin' and request.user.tipoUsuario != 'alumno':
        messages.warning(request, "Permisos de Administrador Requeridos")
        return redirect('inicio')
    else:
        try:
            calificaciones=Calificacion.objects.filter(alumno_id=request.user.id)
            i=0
            promedio=0
            conteo=len(calificaciones)
            while i < conteo:
                promedio+=calificaciones[i].bloque1
                promedio+=calificaciones[i].bloque2
                promedio+=calificaciones[i].bloque3
                promedio+=calificaciones[i].semestral
                i+=1
            promedio=(promedio/(conteo*4))
            promedio=round(promedio, 1)
            color=""
            if promedio<6:
                color="danger"
            elif promedio>=6 and promedio<8:
                color="warning"
            else:
                color="success" 
        except:
            color=""
            promedio=0

    return render(request, 'boleta.html',{
        'calificaciones':calificaciones,
        'promedio':promedio,
        'color':color
    })
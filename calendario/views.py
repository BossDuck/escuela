from django.shortcuts import render, redirect
from django.contrib import messages
from calendario.forms import EventoForm
from calendario.models import EventoCalendario
# Create your views here.


def crearEvento(request):
    if request.user.tipoUsuario != 'admin':
        messages.warning(request, "Permisos de Administrador Requeridos")
        return redirect('inicio')
    else:
        if request.method=='POST':
            titulo=request.POST.get('titulo')
            descripcion=request.POST.get('descripcion')
            fecha=request.POST.get('fecha')
            tipoEvento=request.POST.get('tipoEvento')
            añadir=EventoCalendario(
            titulo=titulo,
            descripcion=descripcion,
            fecha_evento=fecha,
            tipo_evento=tipoEvento)
            añadir.save()
            messages.success(request,"Guardado Correctamente")
            return redirect('añadir-evento')
        

    return render(request, 'crear-evento.html',{
        
    })

def mostrarEventos(request):

    eventos=EventoCalendario.objects.all()

    return render(request, 'listar-eventos.html',{
        'eventos':eventos
    })

def eliminarEvento(request, id):

    if request.user.tipoUsuario != 'admin':
        messages.warning(request, "Permisos de Administrador Requeridos")
        return redirect('inicio')
    else:
        try:
            evento=EventoCalendario.objects.get(id=id)
            evento.delete()
            messages.success(request, "Eliminado Correctamente")
            return redirect('listar-eventos')
        except:
            messages.warning(request, "Error al Eliminar")
            return redirect('listar-eventos')

def editarEvento(request, id):
    if request.user.tipoUsuario != 'admin':
         messages.warning(request, "Permisos de Administrador Requeridos")
         return redirect('inicio')
    else:
        evento=EventoCalendario.objects.get(id=id)
        if request.method=='POST':
            try:
                titulo=request.POST.get('titulo')
                descripcion=request.POST.get('descripcion')
                fecha_evento=request.POST.get('fecha')
                tipo_evento=request.POST.get('tipoEvento')
                EventoCalendario.objects.filter(id=id).update(
                    titulo=titulo,
                    descripcion=descripcion,
                    fecha_evento=fecha_evento,
                    tipo_evento=tipo_evento
                )
                messages.success(request, "Actualizado Corectamente")
                return redirect('listar-eventos')
            except:
                messages.warning(request, "Eror al Actualizar")
                return redirect('listar-eventos')


    return render(request, 'editar-evento.html',{
        'evento':evento
    })




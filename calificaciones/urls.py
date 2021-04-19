from calificaciones import views
from django.urls import path
urlpatterns = [
    path('periodo/añadir/', views.crearPeriodo, name="añadir-periodo"),
    path('periodos/mostrar/', views.mostrarPeriodos, name="listar-periodos"),
    path('periodo/eliminar/<int:id>', views.eliminarPeriodo, name="eliminar-periodo"),
    path('periodo/editar/<int:id>', views.editarPeriodo, name="editar-periodo"),
    path('alumno/calificar/<int:id>', views.calificarAlumno, name="calificar-alumno"),
    path('alumno/boleta/', views.boleta, name="alumno-boleta")
]

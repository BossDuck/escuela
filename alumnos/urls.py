from django.urls import path, include
from alumnos import views
urlpatterns = [
   path('alumnos/añadir/', views.crearAlumno, name="añadir-alumno"),
   path('alumnos/mostrar/', views.mostrarAlumnos, name="listar-alumnos"),
   path('alumnos/eliminar/<int:id>', views.eliminarAlumno, name="eliminar-alumno"),
   path('alumno/editar/<int:id>', views.editarAlumno, name="editar-alumno")
  
]

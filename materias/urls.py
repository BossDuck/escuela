from django.urls import path, include
from materias import views
urlpatterns = [
   path('materias/añadir/', views.crearMateria, name="añadir-materia"),
   path('materias/listar/', views.mostrarMaterias, name="listar-materias"),
   path('eliminar/materia/<int:id>', views.eliminarMateria, name="eliminar-materia"),
   path('editar/materia/<int:id>', views.editarMateria, name="editar-materia")
]

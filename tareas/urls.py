from django.urls import path, include
from tareas import views
urlpatterns = [
   path('tareas/añadir/', views.crearTarea, name="añadir-tarea"),
   path('visualizar-grupos/', views.visualizarGrupos, name="visualizar-grupos"),
   path('visualizar-grupo/<int:id>', views.visualizarGrupo,name="visualizar-grupo"),
   path('tareas/mostrar/<int:id>', views.mostrarTareas, name="listar-tareas"),
   path('tarea/descripcion/<int:id>', views.mostrarTarea , name="descripcion-tarea"),
   path('tareas/listar/', views.listarTareas, name="listar-tareas"),
   path('tarea/eliminar/<int:id>', views.eliminarTarea, name="eliminar-tarea"),
   path('tarea/editar/<int:id>', views.editarTarea, name="editar-tarea")
   
]

from django.urls import path, include
from maestros import views
urlpatterns = [
   path('maestro/añadir/', views.crearMaestro, name="añadir-maestro"),
   path('maestros/mostrar/', views.mostrarMaestros, name="listar-maestros"),
   path('maestros/eliminar/<int:id>', views.eliminarMaestro, name="eliminar-maestro"),
   path('maestros/editar/<int:id>', views.editarMaestro, name="editar-maestro"),
   path('grupo/añadir/', views.crearGrupo, name="añadir-grupo"),
   path('grupos/listar/', views.mostrarGrupos, name="listar-grupos"),
   path('grupos/eliminar/<int:id>', views.eliminarGrupo, name="eliminar-grupo"),
   path('grupos/editar/<int:id>', views.editarGrupo, name="editar-grupo")

]

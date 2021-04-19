from django.urls import path, include
from calendario import views
urlpatterns = [
  path('eventos/añadir/', views.crearEvento, name="añadir-evento"),
  path('eventos/listar/', views.mostrarEventos, name="listar-eventos"),
  path('eventos/eliminar/<int:id>', views.eliminarEvento, name="eliminar-evento"),
  path('evento/editar/<int:id>', views.editarEvento, name="editar-evento")
]

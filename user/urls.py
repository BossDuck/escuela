from django.urls import path, include
from user import views
urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('login/', views.usuariosLogin, name="login"),
    path('logout/', views.usuariosLogout, name="logout")
]

from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('crear_alumno', crear_alumno, name="crear_alumno"),
    path('editar_alumno/<int:id>', editar_alumno, name="editar_alumno"),
    path('eliminar_alumno/<int:id>', eliminar_alumno, name="eliminar_alumno"),
]
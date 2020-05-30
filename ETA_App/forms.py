from django.forms import ModelForm
from .models import Alumno, Usuario

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

class AlumnoForm(ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'apellido', 'calificacion', 'archivo',]
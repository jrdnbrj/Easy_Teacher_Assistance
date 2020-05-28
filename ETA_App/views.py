from django.shortcuts import render, redirect
from .models import Alumno
from .forms import AlumnoForm

# Create your views here.
def index(request):
    alumnos = Alumno.objects.all()
    return render(request, 'index.html', {'alumnos': alumnos})

def crear_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = AlumnoForm()
    return render(request, 'alumno.html', {'form': form, 'title': 'Crear'})


def editar_alumno(request, id):
    alumno = Alumno.objects.get(id = id)
    if request.method == 'GET':
        form = AlumnoForm(instance = alumno)
    else:
        form = AlumnoForm(request.POST, request.FILES, instance = alumno)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return redirect('index')
    return render(request, 'alumno.html', {'form': form, 'title': 'Editar'})

def eliminar_alumno(request, id):
    if request.method == 'POST':
        Alumno.objects.get(id = id).delete()
        return redirect('index')
    return render(request, 'alumno.html', {})
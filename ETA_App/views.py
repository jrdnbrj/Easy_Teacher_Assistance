from django.shortcuts import render, redirect
from .models import Alumno, Usuario
from .forms import AlumnoForm, UsuarioForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    if request.user.is_anonymous:
        alumnos = Alumno.objects.all()
        usuarios = User.objects.all()
        context = {'alumnos': alumnos, 'usuarios': usuarios}
        print('Anonymus')
    else:
        alumnos = Alumno.objects.filter(usuario = request.user)
        context = {'alumnos': alumnos, 'usuarios': User.objects.filter(username = request.user.username)}
    return render(request, 'index.html', context)

def registrar_usuario(request):
    if request.method == 'POST':
        usuario = UsuarioForm(request.POST)
        if usuario.is_valid():
            usuario.save()
        else:
            print('---------------User Error-------------')
        email = request.POST['mail']
        username = request.POST['username']
        password = request.POST['password']
        password_verify = request.POST['password_verify']
        if password == password_verify:
            user = User.objects.create_user(username, email, password)
            if user is None:
                messages.error(request, 'Error al registrar usuario')
        else:
            messages.error(request, 'Las contraseñas no coinciden')
    return redirect('index')

def eliminar_usuario(request):
    try:
        user = User.objects.get(username = request.user.username)
        user.delete()
    except:
        print('-----------Delete User Error-----------')
    return redirect('index')

def iniciar_sesion(request):
    if request.method == 'POST':
        usuario = UsuarioForm(request.POST)
        if usuario.is_valid():
            usuario.save()
        else:
            print('---------------User Error--------------')
        username = request.POST['mail']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
        else:
            messages.error(request, 'Credenciales Incorrectas')
    return redirect('index')

@login_required(login_url = '/')
def cerrar_sesion(request):
    logout(request)
    return redirect('/')

@login_required(login_url = '/')
def crear_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST, request.FILES)
        if form.is_valid():
            alumno = form.save()
            alumno.usuario = request.user
            alumno.save()
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = AlumnoForm()
    return render(request, 'alumno.html', {'form': form, 'title': 'Crear'})

@login_required(login_url = '/')
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

@login_required(login_url = '/')
def eliminar_alumno(request, id):
    if request.method == 'POST':
        Alumno.objects.get(id = id).delete()
        return redirect('index')
    return render(request, 'alumno.html', {})

@login_required(login_url = '/')
def download_file(request, path):
    response = HttpResponse(open('media/' + path, 'rb').read())
    response['Content-Type'] = 'text/plain'
    response['Content-Disposition'] = 'attachment; filename='+path
    return response
from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    return render(request, "aplicacion/base.html")

def profesores(request):
    return render(request, "aplicacion/profesores.html")

def estudiantes(request):
    return render(request, "aplicacion/estudiantes.html")

def entregables(request):
    return render(request, "aplicacion/entregables.html")

def cursos(request):
    ctx = {"cursos": Curso.objects.all() }
    return render(request, "aplicacion/cursos.html", ctx)
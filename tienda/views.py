from django.shortcuts import render, get_object_or_404
from .models import Programa, Curso, Estudiante


def home(request):
    return render(request, "tienda/home.html", {})


"""Vista de inicio"""


"""Vista para listar los programas"""

def lista_programas(request):
    programas = Programa.objects.all().order_by("nombrePrograma")
    return render(request, "tienda/lista_programas.html", {"programas": programas})


"""Vista para mostrar el detalle de un programa"""

def detalle_programa(request, pk):
    programa = get_object_or_404(Programa, pk=pk)
    return render(request, "tienda/detalle_programa.html", {"programa": programa})


"""Vista para listar los cursos"""

def lista_cursos(request):
    cursos = Curso.objects.all().order_by("nombreCurso")
    return render(request, "tienda/lista_cursos.html", {"cursos": cursos})


"""Vista para mostrar el detalle de un curso"""

def detalle_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    return render(request, "tienda/detalle_curso.html", {"curso": curso})


"""Vista para listar los estudiantes"""

def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all().order_by("nombres")
    return render(request, "tienda/lista_estudiantes.html", {"estudiantes": estudiantes})


"""Vista para mostrar el detalle de un estudiante"""

def detalle_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    return render(request, "tienda/detalle_estudiante.html", {"estudiante": estudiante})
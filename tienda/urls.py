from django.urls import path
from . import views

app_name = "tienda"

urlpatterns = [
    path("", views.home, name="home"),
    path("programas/", views.lista_programas, name="lista_programas"),
    path("programas/<int:pk>/", views.detalle_programa, name="detalle_programa"),
    path("cursos/", views.lista_cursos, name="lista_cursos"),
    path("cursos/<int:pk>/", views.detalle_curso, name="detalle_curso"),
    path("estudiantes/", views.lista_estudiantes, name="lista_estudiantes"),
    path("estudiantes/<int:pk>/", views.detalle_estudiante, name="detalle_estudiante"),
]

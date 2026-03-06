from django.db import models

class Programa(models.Model):
    ESTADOS = [
        ("ACTIVO", "Activo"),
        ("INACTIVO", "Inactivo"),
    ]

    nombrePrograma = models.CharField(max_length=150)
    facultad = models.CharField(max_length=150)
    estado = models.CharField(max_length=10, choices=ESTADOS, default="ACTIVO")
    fechaCreacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombrePrograma


class Curso(models.Model):
    ESTADOS = [
        ("ACTIVO", "Activo"),
        ("INACTIVO", "Inactivo"),
    ]

    nombreCurso = models.CharField(max_length=150)
    codigoCurso = models.CharField(max_length=20, unique=True)
    creditos = models.PositiveIntegerField()
    estado = models.CharField(max_length=10, choices=ESTADOS, default="ACTIVO")
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE, related_name="cursos", null=True)

    def __str__(self):
        return f"{self.codigoCurso} - {self.nombreCurso}"

class Estudiante(models.Model):
    ESTADOS = [
        ("ACTIVO", "Activo"),
        ("INACTIVO", "Inactivo"),
        ("GRADUADO", "Graduado"),
    ]

    nombres = models.CharField(max_length=150)
    cedula = models.CharField(max_length=20, unique=True)
    programa = models.ForeignKey(Programa, on_delete=models.SET_NULL, null=True, related_name="estudiantes")
    estado = models.CharField(max_length=10, choices=ESTADOS, default="ACTIVO")

    def __str__(self):
        return f"{self.nombres} - {self.cedula}"
    

class Inscripcion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='inscripciones')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='inscripciones')
    fecha = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('estudiante', 'curso')

    def __str__(self):
        return f"{self.estudiante.nombres} - {self.curso.nombreCurso}"

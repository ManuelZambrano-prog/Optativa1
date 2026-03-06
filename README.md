Readme · MD
Copiar

# Universidad - Sistema de Gestión Académica

Aplicación web desarrollada con **Django** que permite gestionar la información académica básica de una universidad: programas, cursos y estudiantes, incluyendo la relación de inscripciones entre estudiantes y cursos.

---

## Tecnologías utilizadas

- Python 3.12
- Django 5.0
- SQLite (base de datos)
- HTML + CSS (templates de Django)

---

## Estructura del proyecto

```
Optativa1/
├── core/               # Configuración principal del proyecto
│   ├── settings.py
│   └── urls.py
├── tienda/             # App principal
│   ├── models.py       # Modelos: Programa, Curso, Estudiante, Inscripcion
│   ├── views.py        # Vistas de lista y detalle
│   ├── urls.py         # Rutas de la app
│   ├── static/css/     # Estilos CSS
│   └── templates/      # Plantillas HTML
├── manage.py
└── requirements.txt
```

---

## Modelos

| Modelo | Descripción |
|--------|-------------|
| `Programa` | Carrera universitaria con nombre, facultad y estado |
| `Curso` | Materia con código, créditos y programa al que pertenece |
| `Estudiante` | Estudiante con cédula, nombre, programa y estado |
| `Inscripcion` | Relación única entre un estudiante y un curso |

### Reglas de negocio
- Un Programa tiene muchos Cursos
- Un Curso pertenece a un Programa
- Un Estudiante puede inscribirse a varios Cursos
- Un Curso puede tener varios Estudiantes
- Una pareja (estudiante, curso) no se puede repetir

---

## Instalación y ejecución

### 1. Clonar el repositorio
```bash
git clone https://github.com/ManuelZambrano-prog/Optativa1.git
cd Optativa1
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Aplicar migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Poblar la base de datos (opcional)
```bash
python manage.py shell < tienda/making_queries.py
```

### 5. Correr el servidor
```bash
python manage.py runserver
```

### 6. Abrir en el navegador
```
http://127.0.0.1:8000/
```

---

## Vistas disponibles

| URL | Descripción |
|-----|-------------|
| `/` | Página de inicio |
| `/programas/` | Lista de todos los programas |
| `/programas/<id>/` | Detalle de un programa con sus cursos |
| `/cursos/` | Lista de todos los cursos |
| `/cursos/<id>/` | Detalle de un curso con estudiantes inscritos |
| `/estudiantes/` | Lista de todos los estudiantes |
| `/estudiantes/<id>/` | Detalle de un estudiante con sus cursos inscritos |

---

## Autor

**Manuel Zambrano**  
GitHub: [@ManuelZambrano-prog](https://github.com/ManuelZambrano-prog)

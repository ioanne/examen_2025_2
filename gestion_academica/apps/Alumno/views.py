from django.views.generic import ListView, DetailView
from .models import Alumno

class AlumnoListView(ListView):
    model = Alumno
    template_name = "AlumnoListView.html" 
    context_object_name = "alumnos"

class AlumnoDetailView(DetailView):
    model = Alumno
    template_name = "AlumnoDetalleView.html" 
    context_object_name = "alumno"


from django.db.utils import OperationalError
from .models import Alumno

try:
    if Alumno.objects.count() == 0:
        Alumno.objects.create(
            nombre="Sofía",
            apellido="Gómez",
            email="sofia.gomez@example.com",
            legajo=1001
        )
        Alumno.objects.create(
            nombre="Matías",
            apellido="Rodríguez",
            email="matias.rodriguez@example.com",
            legajo=1002
        )
        Alumno.objects.create(
            nombre="Lucía",
            apellido="Fernández",
            email="lucia.fernandez@example.com",
            legajo=1003
        )
except OperationalError:

    pass

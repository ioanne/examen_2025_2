from django.shortcuts import ListView, DetailView
from .models import Alumno

class AlumnoListView(ListView):
    model = Alumno
    template_name = 'alumnos/lista_alumnos.html'
    context_object_name = 'alumnos'

class AlumnoDetalleView(DetailView):
    model = Alumno
    template_name = 'alumnos/detalle_alumno.html'

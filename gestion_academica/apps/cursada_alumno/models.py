from django.db import models
from apps.Alumno.models import Alumno
from apps.cursada.models import Cursada

class CursadaAlumno(models.Model):
    id_alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, related_name='alumno_cursada')
    id_cursada = models.ForeignKey(Cursada, on_delete=models.CASCADE, related_name='alumno_cursada')
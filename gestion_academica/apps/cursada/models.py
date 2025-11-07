from django.db import models
from apps.profesor.models import Profesor
from apps.asignatura.models import Asignatura

class Cursada(models.Model):
    ESTADOS = [
        ('Activa', 'Activa'),
        ('Finalizada', 'Finalizada'),
    ]

    nombre = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='Activa')

    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, related_name='cursada')
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE, related_name='cursada')

    def __str__(self):
        return f"{self.nombre} ({self.estado})"
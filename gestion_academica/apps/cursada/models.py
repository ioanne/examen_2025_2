from django.db import models

class Cursada(models.Model):
    ESTADOS = [
        ('Activa', 'Activa'),
        ('Finalizada', 'Finalizada'),
    ]

    nombre = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='Activa')

    def __str__(self):
        return f"{self.nombre} ({self.estado})"
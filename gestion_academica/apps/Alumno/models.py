from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    numero_id = models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

from django.db import models

class Alumno(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    legajo = models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

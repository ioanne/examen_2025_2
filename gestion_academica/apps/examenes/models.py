from django.db import models

class Examen(models.Model):
    id = models.BigAutoField(editable=False, unique=True, primary_key=True )
    titulo = models.CharField("título del examen", max_length=200)
    asignatura = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

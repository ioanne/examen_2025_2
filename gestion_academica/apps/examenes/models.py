from django.db import models

class Examen(models.Model):
    titulo = models.CharField("título del examen", max_length=200)
    fecha_creacion = models.DateTimeField(auto_now_add=True)



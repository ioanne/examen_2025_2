from django.db import models

# Create your models here.
class Pregunta(models.Model):
    examen = models.ForeignKey('examenes.Examen', on_delete=models.CASCADE, related_name='preguntas')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    
    def __str__(self):
        return self.titulo

class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name='respuestas')
    texto_respuesta = models.TextField(blank=True)
    es_correcta = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Respuesta a: {self.pregunta.titulo}"
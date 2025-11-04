from django.shortcuts import render
from .models import Examen
from django.http import JsonResponse

# Create your views here.

def lista_examenes(request):
    print("Accediendo a la vista lista_examenes")   
    examenes = Examen.objects.all().order_by('-fecha_creacion')
    data = [
        {
            "id": examen.id,
            "titulo": examen.titulo,
            "fecha_creacion": examen.fecha_creacion.strftime("%Y-%m-%d %H:%M:%S")
        }
        for examen in examenes
    ]
    return JsonResponse(data, safe=False)


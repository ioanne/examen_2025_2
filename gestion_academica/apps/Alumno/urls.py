from django.urls import path
from .views import AlumnoListView, AlumnoDetailView

urlpatterns = [
    path('', AlumnoListView.as_view(), name='lista_alumnos'),
    path('<int:pk>/', AlumnoDetailView.as_view(), name='detalle_alumno'),
]
from django.urls import path
from .views import AlumnoListView, AlumnoDetailView, AlumnoCreateView

urlpatterns = [
    path('', AlumnoListView.as_view(), name='lista_alumnos'),
    path('<int:pk>/', AlumnoDetailView.as_view(), name='detalle_alumno'),
    path('nuevo/', AlumnoCreateView.as_view(), name='crear_alumno'),
]
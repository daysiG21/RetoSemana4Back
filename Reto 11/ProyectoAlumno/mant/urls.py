from django.urls import path
from .views import ListarAlumnocontroller, CRUDAlumnoController

urlpatterns =[
  path('alumnos',ListarAlumnocontroller.as_view()),
  path('alumnos/<int:pk>', CRUDAlumnoController.as_view()),
]
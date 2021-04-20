from django.db.models import query
from .serializers import MostrarAlumnosSerializer
from .models import AlumnoModel
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.response import Response

class ListarAlumnocontroller(ListCreateAPIView):
  queryset=AlumnoModel.objects.all()
  serializer_class=MostrarAlumnosSerializer


class CRUDAlumnoController(RetrieveUpdateDestroyAPIView):
  queryset = AlumnoModel.objects.all()
  serializer_class = MostrarAlumnosSerializer
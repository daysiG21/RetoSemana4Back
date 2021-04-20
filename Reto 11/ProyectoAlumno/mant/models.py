from django.db import models

# Create your models here.

class AlumnoModel(models.Model):
  alumnoId = models.AutoField(
    primary_key=True,
    unique = True,
    null = False,
    db_column = 'id'
  )
  alumnoNombre = models.CharField(
    max_length=100,
    null = False,
    db_column ='nombres',
    verbose_name='Nombres',
    help_text='Ingrese el nombre'
  )
  alumnoApePaterno = models.CharField(
    max_length=100,
    db_column='apePat',
    verbose_name='Apellidos',
    help_text='Ingrese el apellido paterno'
  )
  alumnoApeMaterno=models.CharField(
    max_length=100,
    db_column='apeMat',
    verbose_name='Apellido Materno',
    help_text='Ingrese el apellido materno'
  )
  class Meta:
    db_table='alumno'
    verbose_name='alumno'
    verbose_name_plural='alumnos'
  
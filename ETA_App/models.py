from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Alumno(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    calificacion = models.DecimalField("Calificación", max_digits=4, decimal_places=2)
    archivo = models.FileField(upload_to='', max_length=None, null=True, blank=True)
    usuario = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + ' ' + self.apellido + ' -> ' + str(self.calificacion)
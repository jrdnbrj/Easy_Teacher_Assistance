from django.db import models

# Create your models here.

class Alumno(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    calificacion = models.DecimalField(max_digits=4, decimal_places=2)
    archivo = models.FileField(upload_to='', max_length=None, null=True, blank=True)

    def __str__(self):
        return self.nombre + ' ' + self.apellido + ' -> ' + str(self.calificacion)
from django.db import models

# Create your models here.

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    editorial = models.CharField(max_length=50)
    anio_publicacion = models.IntegerField()

    def __str__(self):
        return self.titulo
    
class Usuario(models.Model):
    usuario = models.CharField(max_length=64)
    contrasena = models.CharField(max_length=64)
    
    def __str__(self):
        return self.usuario
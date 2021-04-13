from django.db import models
from django.urls import reverse

# Create your models here.
class Organizadores(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre




class Juegos(models.Model):
    juego = models.CharField(max_length=200)
    edades = models.CharField(max_length=200)
    organizador = models.ForeignKey(
        Organizadores,
        on_delete=models.CASCADE,
    )
    descripcion = models.TextField()

    def __str__(self):
        return self.juego

    def get_absolute_url(self):
        return reverse('detalleJuego', args=[str(self.id)])

    fotos = models.CharField(max_length=200, default='')


from django.db import models

# Create your models here.

class Prueba(models.Model):
    titulo = models.CharField('Titulo', max_length=50)
    subtitulo = models.CharField('Sub titulo', max_length=50)
    cantidad = models.IntegerField()

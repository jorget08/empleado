from django.db import models
from applications.departamento.models import Departamento

#app de terceros, esto sera para agregar un editor al admin
from ckeditor.fields import RichTextField
# Create your models here.

class Habilidades(models.Model):
    hablidad = models.CharField('Habilidad', max_length=50)

    class meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleados'
    
    def __str__(self):
        return str(self.id) + '-' + self.hablidad



class Empleado(models.Model):
    first_name = models.CharField('Nombres', max_length=50)
    last_name = models.CharField('Apellidos', max_length=50)
    job = models.CharField('Trabajo', max_length=50)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    #guardará la imagen en la carpeta empleado que esta dentro de la carpeta media que ya especificamos en el local.py
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)
    
    full_name = models.CharField(max_length=120, blank=True)
    #Editor
    hoja_vida = RichTextField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['first_name']

        
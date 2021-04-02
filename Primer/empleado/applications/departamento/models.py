from django.db import models

# Create your models here.

class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50)
    short_name = models.CharField("Nombre Corto", max_length=50)
    anulate = models.BooleanField("Anulado", default = False)

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

        #ordering = ['aqui va el parametro por el que lo quiero ordenar, en este caso: name, short_name o anulate']

        #Esto hace que no se pueda crear algun otro objeto con los mismos atributos (name y short_name), si ya 
        #existe un objeto creado con esos atributos[(PERFECTOS PARA PONER EN CEDULA Y QUE NO SE REPITAN LOS DEUDORES)]
        unique_together = ('name', 'short_name')

    """Como se muestra en el admin de django se vera algo asi: 1-contabilidad"""
    def __str__(self):
        return str(self.id) + '-' + self.short_name
    
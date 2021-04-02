from django.contrib import admin
from .models import Departamento
# Register your models here.

"""Esta forma me permite como se va a mostrar en el listado del objeto"""
@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'short_name', 'anulate'
    )
    #Añadimos un buscador y decimos por que argumento realizar busquedas
    search_fields = ('short_name',)

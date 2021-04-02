from django.contrib import admin
from .models import Empleado, Habilidades
# Register your models here.

admin.site.register(Habilidades)


"""Esta forma me permite como se va a mostrar en el listado del objeto"""
@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'departamento', 
        'job',

        #Este es un campo que no esta en el modelo pero queremos añadirlo para que sea vea en el admin
        #podria ser para sumar colunmas como por ejemplo ahora que lo pondremos para que muestr el nombre completo en
        'fullname',
    )

    #Para la columna full_name que no esta en nuestro modelo sino que queremos ponerla debemos hacer lo siguiente:
    def fullname(self, obj):
        return obj.first_name + ' ' + obj.last_name


    #Añadimos buscador a admin y le decimos por que argumentos puede realizar busquedas
    search_fields = ('first_name',)

    #Añadimos un filtro en admin y le decimos sobre que argumentos queremos que se pueda filtrar
    list_filter = ('job', 'habilidades')

    #Este campo solo sirve para lo que son relaciones (manytomany, foreginkey y onetoonefield) y es un filtrado
    #para cuando queremos, desde el admin de django, hacer alguna relacion creando un objeto o algo y que sea mas facil
    #encontrar la que queremos
    filter_horizontal = ('habilidades',)






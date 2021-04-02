from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic import ListView
from .forms import NewDptoYPersonaForm
from .models import Departamento
from applications.persona.models import Empleado
# Create your views here.

#Vamos a registrar no solo un departamento sino tambien a un empleado
class NewDptoYPersonaView(FormView):
    template_name = 'departamento/new.html'
    form_class = NewDptoYPersonaForm
    success_url = '/'

    #En FormView se debe sobreescribir este metodo
    def form_valid(self, form):

        #Primero voy a interceptar los datos y regustrarlos.
        #Como el empleado debe tener un departamento guardamos primero dpto.

        #Creamos un objeto departamento que debe tener un name y un short_name pues asi lo requiere el modelo
        depa = Departamento(
            #le digo que el name sera igual al parametro que estan pasando en el formulario cmo departamento
            name = form.cleaned_data['departamento'],

            #le digo que el short_name sera el que se esta pasando en el formulario como short_name
            short_name = form.cleaned_data['short_name']
        )
        #Ahora le digo que guarde en la base de datos y se ha creado ese departamento
        depa.save()


        #Ahora voy a guardar al empleado que tiene que ir con ese departamento, empleado tiene en modelo como obligatorio
        #first_name, last_name, job, departamento y son los que pondremos, en el formulario no pusismos que metieran job
        #asi que le pondremos aqui cualquier cosa para no hacer mas trabajo en ir a poner en el form xD
        Empleado.objects.create(
            first_name = form.cleaned_data['nombre'],
            last_name = form.cleaned_data['apellidos'],
            job = 'albañil',
            #le decimos que el dpto sera el depa que ya guardamos arriba
            departamento = depa
        )
        """Como en esta ocacion usamos create, esto se guarda de forma automatica y no necesitamos guardar con save() como en depa"""

        return super(NewDptoYPersonaView, self).form_valid(form)


"""Vista para listar departamentos"""


class DptListView(ListView):
    template_name = "departamento/lista.html"
    model = Departamento
    context_object_name = 'departamentos'

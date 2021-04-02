from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView, DeleteView
from django.urls import reverse_lazy

from .forms import EmpleadoForm
from .models import Empleado, Habilidades
# Create your views here.

"""Lista todos los empleados de la empresa"""
class ListAllListView(ListView):
    template_name = "persona/list_all.html"
    paginate_by = 4
    ordering = 'id'
    context_object_name = 'persona'
    
    def get_queryset(self):

        #Con esto le estamos diciendo que atrape lo que nos dan por el metodo get (<input type="text" id="keyword" name="keyword")
        #osea eso, lo que ingresan en ese campo (keyword); GET (el metodo que se esta usando)
        keyword = self.request.GET.get('keyword', '')

        #La lista sera el objeto empleado que tenga como full_name(atributo de su modelo) lo missmo que el keyword sea uno solo o 
        #varios los que se llamen asi; el icontains nos va a ayudar para mostrar cualquiera que tenga como nombre completo (que estamos buscando)
        #lo que el usuario ingrese en el input
        lista = Empleado.objects.filter(full_name__icontains = keyword)

        return lista


"""Lista los empleados del area"""
class ListArea(ListView):
    template_name = "persona/list_dep.html"
    context_object_name = 'persona'

    def get_queryset(self):
        #Aqui optenemos lo que no pasa por la url
        dpto = self.kwargs['shortname']

        lista = Empleado.objects.filter(departamento__short_name = dpto)
        return lista


"""Lista empleados por palabra clave ---- Se muestra la busqueda ahi mismo"""
class ListByKeyword(ListView):
    template_name = "persona/by-keyword.html"
    context_object_name = 'persona'

    def get_queryset(self):

        #Con esto le estamos diciendo que atrape lo que nos dan por el metodo get (<input type="text" id="keyword" name="keyword")
        #osea eso, lo que ingresan en ese campo (keyword)
        kword = self.request.GET.get('keyword',)

        #La lista sera el objeto empleado que tenga como first_name(atributo de su modelo) lo missmo que el kword sea uno solo o 
        #varios que se llamen asi
        lista = Empleado.objects.filter(first_name = kword)

        return lista


"""Muestra las habilidades del empelado con el id dado"""
class ListaHabilidades(ListView):
    template_name = "persona/lista-habilidades.html"
    context_object_name = 'habilidades'

    def get_queryset(self):

        #Le digo que traiga el objeto Empleado que tiene ese id y lo guarde en un variable llamada empleado
        empleado = Empleado.objects.get(id=3)
        
        #Retorno todas las habilidades, de esta forma ya que empleado esta relacionado con habilidades de muchos a muchos
        return empleado.habilidades.all()
    
    

class EmpleadoDetailView(DetailView):
    template_name = "persona/detail-empleado.html"
    model = Empleado
    context_object_name = 'persona'



class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/add-empleado.html"
    form_class = EmpleadoForm
    #fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidades', 'avatar'] #para el __all__ se usan los () asi: ("__all__"); para indicar uno mismo los campos se usan ['']
    success_url = reverse_lazy('persona_app:listar-todo')

    #Tenos un campo en el modelo llamado full_name y vamos a llenarlo con el nombre y el apellido que nos dan por el formulario
    #Lo que hacemos es sobreescribir esta funcion la cual valida que lo que llenan es vaido, osea cumple con los max_length y eso
    def form_valid(self,form):

        #Aqui le digo que los datos que ingresaron (antes de ser guardados en la db), que los tenga en una variable empleado (para
        # no tener que realizar una busqueda y eso)
        empleado = form.save(commit=False)

        #Le digo que el campo full_name que tenemos en el modelo lo va a llenar con el nombre y apellidos
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name

        #Le digo que lo guarde en la base de datos
        empleado.save()

        return super().form_valid(form)



class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/update.html"
    fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidades'] #para el __all__ se usan los () asi: ("__all__"); para indicar uno mismo los campos se usan ['']
    success_url = reverse_lazy('persona_app:lista_admin')



class HomeView(TemplateView):
    template_name = "home.html"



"""Vista administrar"""

class ListaEmpleadosAdmin(ListView):
    template_name = "persona/lista-admin.html"
    paginate_by = 10
    context_object_name = 'persona'
    model = Empleado


"""Vista para eleiminar empleado"""

class EmpleadoDelete(DeleteView):
    template_name = "persona/delete.html"
    model = Empleado
    success_url = reverse_lazy('persona_app:lista_admin')

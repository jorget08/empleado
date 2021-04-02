from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from .forms import PruebaForm
from .models import Prueba
# Create your views here.


class PruebaUpdateView(CreateView):
    model_form = Prueba
    form_class = PruebaForm
    template_name = "prueba/update.html"
    success_url = reverse_lazy('prueba_app:update')


class PruebaCss(TemplateView):
    template_name = "prueba/prueba-static.html"

class PruebaGrillas(TemplateView):
    template_name = "prueba/prueba-grillas.html"
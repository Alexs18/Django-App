from django.shortcuts import render
from django.views.generic import TemplateView, ListView
# Create your views here.

#Renderizamos la vista por medio de un template
class Home(TemplateView):
    template_name: str = 'home/home.html'

class Formulario(TemplateView):
    template_name: str = 'home/formulario.html'

class ListaProductos(ListView):
    template_name: str = 'home/ListaProductos.html'
    queryset = ['PESCADO', 'ARROZ', 'CEVICHE']
    context_object_name = 'LISTAPRODUCTOS'
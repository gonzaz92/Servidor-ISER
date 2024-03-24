from django.shortcuts import render
from .models import Libro, Acta
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from .forms import ActaForm, ActaUpdate
from django.urls import reverse_lazy
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, user_passes_test
import locale

institutos = Libro.objects.all()

def libros(request):
    return render(request, 'Libros/libros.html')

def prueba(request):
    institutos
    return render(request, 'Libros/acta_form.html', {'institutos' : institutos})

class NuevoLibro(CreateView):
    model = Libro
    fields = '__all__'
    success_url = reverse_lazy('libros')

class ListarLibros(ListView):
    model = Libro
    fields = '__all__'
    success_url = reverse_lazy('libros')

class ActualizarLibro(UpdateView):
    model = Libro
    fields = '__all__'
    success_url = reverse_lazy('libros')

#################Actas#####################

class NuevaActa (CreateView):
    template_name = 'Libros/acta_form.html'
    form_class = ActaForm
    success_url = reverse_lazy('libros')

class ListarActas(ListView):
    model = Acta
    fields = '__all__'
    template_name = 'Libros/acta_list.html'

    def get_queryset(self):
        nombre = self.kwargs['nombre']
        return Acta.objects.filter(instituto = nombre)

class DetalleActa(DetailView):
    model = Acta

class ActualizarActa(UpdateView):
    model = Acta
    success_url = reverse_lazy('libros')
    form_class = ActaUpdate
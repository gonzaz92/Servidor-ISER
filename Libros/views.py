from django.shortcuts import render
from .models import Libro, Acta, Firma
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from .forms import ActaForm, ActaUpdate
from django.urls import reverse_lazy
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse

########### Permisos ##########

def nuevo_libro(user):
    return user.has_perm('Libros.add_libro')

def ver_libro(user):
    return user.has_perm('Libros.view_libro')


def nueva_acta(user):
    return user.has_perm('Libros.add_acta')

def actualizar_acta(user):
    return user.has_perm('Libros.change_acta')

#################################################################

@login_required
def libros(request):
    return render(request, 'Libros/libros.html')

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(nuevo_libro), name='get')
class NuevoLibro(CreateView):
    model = Libro
    fields = '__all__'
    success_url = reverse_lazy('libros')

@method_decorator(login_required, name='get')
class ListarLibros(ListView):
    model = Libro
    fields = '__all__'
    success_url = reverse_lazy('libros')

@method_decorator(login_required, name='get')
class ActualizarLibro(UpdateView):
    model = Libro
    fields = '__all__'
    success_url = reverse_lazy('libros')

#################Actas#####################

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(nueva_acta), name='get')
class NuevaActa(CreateView):
    template_name = 'Libros/acta_form.html'
    form_class = ActaForm
    success_url = reverse_lazy('libros')

    def firmo(self):
        firmascargadas = Firma.objects.values_list('id', 'user__last_name', 'user__first_name')
        firmas = []
        for firm in firmascargadas:
            firmas.append(firm)
        return firmas

    def listado(self):
        institutos = Libro.objects.values_list('nombre', flat=True)
        opciones = []
        for insti in institutos:
            opciones.append(insti)
        return opciones

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['opciones'] = self.listado()
        context['firmas'] = self.firmo()
        return context

@method_decorator(login_required, name='get')
class ListarActas(ListView):
    model = Acta
    fields = '__all__'
    template_name = 'Libros/acta_list.html'

    def get_queryset(self):
        nombre = self.kwargs['nombre']
        return Acta.objects.filter(instituto = nombre).order_by('-fecha')

@method_decorator(login_required, name='get')
class DetalleActa(DetailView):
    model = Acta

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(actualizar_acta), name='get')
class ActualizarActa(UpdateView):
    model = Acta
    success_url = reverse_lazy('libros')
    form_class = ActaUpdate
    
    def firmo(self):
        firmascargadas = Firma.objects.values_list('id', 'user__last_name', 'user__first_name')
        firmas = []
        for firm in firmascargadas:
            firmas.append(firm)
        return firmas

    def listado(self):
        institutos = Libro.objects.values_list('nombre', flat=True)
        opciones = []
        for insti in institutos:
            opciones.append(insti)
        return opciones

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['opciones'] = self.listado()
        context['firmas'] = self.firmo()
        return context
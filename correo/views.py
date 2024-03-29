from django.shortcuts import render
from correo.forms import CorreoForm, CorreoUpdate
from correo.models import Correo
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.db.models import Q

def permiso_carga(user):
    return user.has_perm('correo.add_correo')

def permiso_ver(user):
    return user.has_perm('correo.view_correo')

def permiso_actualizar(user):
    return user.has_perm('correo.change_correo')

def permiso_borrar(user):
    return user.has_perm('correo.delete_correo')

@login_required
def correo(request):
    return render(request, 'correo/correo.html')

@login_required
@user_passes_test(permiso_ver)
def buscar_envio(request):
    query = request.GET.get('q')
    resultados_correo = Correo.objects.filter(Q(destinatario__icontains=query) | Q(nombre__icontains=query) |
                                                Q(dni__icontains=query) | Q(categoria__icontains=query) | Q(carnet__icontains=query))
    return render(request, 'correo/resultados_correo.html', {'resultados_correo': resultados_correo})

@login_required
@user_passes_test(permiso_ver)
def correo_finalizados(request):
    corre = Correo.objects.all().order_by('-envio')
    return render(request, 'correo/correo_finalizados.html', {'corre' : corre})

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(permiso_carga), name='get')
class NuevoEnvio(CreateView):
    template_name = 'correo/correo_form.html'
    form_class = CorreoForm
    success_url = reverse_lazy('correo')

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(permiso_ver), name='get')
class ListarCorreo(ListView):
    model = Correo
    fields = '__all__'

    def get_queryset(self):
        return Correo.objects.all().order_by('-envio')

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(permiso_actualizar), name='get')
class ActualizarCorreo(UpdateView):
    model = Correo
    success_url = reverse_lazy('correo')
    form_class = CorreoUpdate

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(permiso_borrar), name='get')
class CorreoBorrar(DeleteView):
    model = Correo
    success_url = reverse_lazy('correo')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['envio'] = Correo.objects.get(pk=self.kwargs['pk'])
        return context
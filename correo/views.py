from django.shortcuts import render
from correo.forms import CorreoForm
from correo.models import Correo
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

def correo(request):
    return render(request, 'correo/correo.html')

def correo_finalizados(request):
    corre = Correo.objects.all()
    return render(request, 'correo/correo_finalizados.html', {'corre' : corre})

class NuevoEnvio(CreateView):
    template_name = 'correo/correo_form.html'
    form_class = CorreoForm
    success_url = reverse_lazy('correo')

class ListarCorreo(ListView):
    model = Correo
    fields = Correo.envio, Correo.seguimiento, Correo.destinatario, Correo.direccion

class ActualizarCorreo(UpdateView):
    model = Correo
    success_url = reverse_lazy('correo')
    fields = '__all__'
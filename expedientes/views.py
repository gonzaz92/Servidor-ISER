from django.shortcuts import render
from expedientes.forms import ExpedienteForm
from expedientes.models import Expediente
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator

@login_required
def expedientes(request):
    return render(request, 'expedientes/expedientes.html')

class CrearExpediente(CreateView):
    template_name = 'expedientes/expediente_form.html'
    form_class = ExpedienteForm
    success_url = reverse_lazy('expedientes')

class ListarExpedientes(ListView):
    model = Expediente
    fields = Expediente.Año_de_Expediente, Expediente.Número_de_Expediente, Expediente.Categoría, Expediente.Instituto_o_Localidad, Expediente.Fecha_de_Creación, Expediente.Estado
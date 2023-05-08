from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from Base_datos.models import Locutor_nacional, Locutor_local, Operador_nacional_radio, Operador_nacional_tv, Operador_nacional_planta, Operador_local_radio, Operador_local_tv, Operador_local_planta, Productor, Guionista
from Base_datos.forms import UsuarioForm
from django.db.models import Q

def index(request):
    return render(request, 'Base_datos/index.html')

def locutores(request):
    return render(request, 'Base_datos/locutores_nacionales.html')

def ln_incompletos(request):
    ln = Locutor_nacional.objects.all()
    return render(request, 'Base_datos/ln_incompletos.html', {'ln' : ln} )

class UserSingUp(LoginRequiredMixin, CreateView):
    form_class = UsuarioForm
    template_name = 'registration/singup.html'
    success_url = reverse_lazy('mi_blog_listar')

class UserLogin(LoginView):
    next_page = reverse_lazy('mi_blog_listar')

class UserLogout(LogoutView):
    next_page = reverse_lazy('mi_blog_index')


class CrearLocutorNacional(CreateView):
    model = Locutor_nacional
    success_url = reverse_lazy('locutores_nacionales')
    fields = '__all__'

class ListarLocutorNacional(ListView):
    model = Locutor_nacional
    fields = Locutor_nacional.apellido, Locutor_nacional.nombre, Locutor_nacional.DNI, Locutor_nacional.habilitación, Locutor_nacional.instituto, Locutor_nacional.expediente, Locutor_nacional.disposición

class VerLocutorNacional(DetailView):
    model = Locutor_nacional
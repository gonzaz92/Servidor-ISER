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

def buscar(request):
    query = request.GET.get('q')
    resultados_ln = Locutor_nacional.objects.filter(Q(apellido__icontains=query) | Q(nombre__icontains=query) | Q(DNI__icontains=query) | Q(id__icontains=query))
    resultados_ll = Locutor_local.objects.filter(Q(apellido__icontains=query) | Q(nombre__icontains=query) | Q(dni__icontains=query) | Q(id__icontains=query))
    resultados = list(resultados_ln) + list(resultados_ll)
    return render(request, 'Base_datos/resultados_busqueda.html', {'resultados':resultados})

"""class UserSingUp(LoginRequiredMixin, CreateView):
    form_class = UsuarioForm
    template_name = 'registration/singup.html'
    success_url = reverse_lazy('mi_blog_listar')

class UserLogin(LoginView):
    next_page = reverse_lazy('mi_blog_listar')

class UserLogout(LogoutView):
    next_page = reverse_lazy('mi_blog_index')"""

#Locutores Nacionales

def locutores(request):
    return render(request, 'Base_datos/locutores_nacionales.html')

def ln_incompletos(request):
    ln = Locutor_nacional.objects.all()
    return render(request, 'Base_datos/ln_incompletos.html', {'ln' : ln} )

class CrearLocutorNacional(CreateView):
    model = Locutor_nacional
    success_url = reverse_lazy('locutores_nacionales')
    fields = '__all__'

class ListarLocutorNacional(ListView):
    model = Locutor_nacional
    fields = (Locutor_nacional.apellido, Locutor_nacional.nombre, Locutor_nacional.DNI, Locutor_nacional.habilitación, Locutor_nacional.instituto,
        Locutor_nacional.año_expediente, Locutor_nacional.número_expediente,Locutor_nacional.año_disposición, Locutor_nacional.número_disposición)

class VerLocutorNacional(DetailView):
    model = Locutor_nacional

class ActualizarLN(UpdateView):
    model = Locutor_nacional
    success_url = reverse_lazy('locutores_nacionales')
    fields = '__all__'

#Locutores Locales

def locutor_local(request):
    return render(request, 'Base_datos/locutores_locales.html')

def ll_incompletos(request):
    ll = Locutor_local.objects.all()
    return render(request, 'Base_datos/ll_incompletos.html', {'ll' : ll} )

class CrearLocutorLocal(CreateView):
    model = Locutor_local
    success_url = reverse_lazy('locutores_locales')
    fields = '__all__'

class ListarLocutorLocal(ListView):
    model = Locutor_local
    fields = (Locutor_local.apellido, Locutor_local.nombre, Locutor_local.DNI, Locutor_local.habilitación, Locutor_local.localidad, Locutor_local.provincia,
        Locutor_local.año_expediente, Locutor_local.número_expediente,Locutor_local.año_disposición, Locutor_local.número_disposición)

class VerLocutorLocal(DetailView):
    model = Locutor_local
    
class ActualizarLL(UpdateView):
    model = Locutor_local
    success_url = reverse_lazy('locutores_locales')
    fields = '__all__'
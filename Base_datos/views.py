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
    resultados_ln = Locutor_nacional.objects.filter(Q(apellido__icontains=query) | Q(nombre__icontains=query) | Q(DNI__icontains=query))
    resultados_ll = Locutor_local.objects.filter(Q(apellido__icontains=query) | Q(nombre__icontains=query) | Q(DNI__icontains=query))
    resultados_oprn = Operador_nacional_radio.objects.filter(Q(apellido__icontains=query) | Q(nombre__icontains=query) | Q(DNI__icontains=query))
    resultados = list(resultados_ln) + list(resultados_ll) + list(resultados_oprn)
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

#Operadores Nacionales

def operadores_nacionales(request):
    return render(request, 'Base_datos/operadores_nacionales.html')

#Operadores de Radio

def oprn_incompletos(request):
    oprn = Operador_nacional_radio.objects.all()
    return render(request, 'Base_datos/oprn_incompletos.html', {'oprn' : oprn} )

class CrearOperadordeRadio(CreateView):
    model = Operador_nacional_radio
    success_url = reverse_lazy('operadores_nacionales')
    fields = '__all__'

class ListarOperadordeRadio(ListView):
    model = Operador_nacional_radio
    fields = (Operador_nacional_radio.apellido, Operador_nacional_radio.nombre, Operador_nacional_radio.DNI, Operador_nacional_radio.habilitación, Operador_nacional_radio.instituto,
              Operador_nacional_radio.año_expediente, Operador_nacional_radio.número_expediente, Operador_nacional_radio.año_disposición, Operador_nacional_radio.número_disposición)

class VerOperadordeRadio(DetailView):
    model = Operador_nacional_radio

class ActualizarOPR(UpdateView):
    model = Operador_nacional_radio
    success_url = reverse_lazy('operadores_nacionales')
    fields = '__all__'

#Operadores de TV

def optvn_incompletos(request):
    optvn = Operador_nacional_tv.objects.all()
    return render(request, 'Base_datos/optvn_incompletos.html', {'oprn' : optvn} )

class CrearOperadordeTV(CreateView):
    model = Operador_nacional_tv
    success_url = reverse_lazy('operadores_nacionales')
    fields = '__all__'

class ListarOperadordeTV(ListView):
    model = Operador_nacional_tv
    fields = (Operador_nacional_tv.apellido, Operador_nacional_tv.nombre, Operador_nacional_tv.DNI, Operador_nacional_tv.habilitación, Operador_nacional_tv.instituto,
              Operador_nacional_tv.año_expediente, Operador_nacional_tv.número_expediente, Operador_nacional_tv.año_disposición, Operador_nacional_tv.número_disposición)

class VerOperadordeTV(DetailView):
    model = Operador_nacional_tv

class ActualizarOPTV(UpdateView):
    model = Operador_nacional_tv
    success_url = reverse_lazy('operadores_nacionales')
    fields = '__all__'

#Operadores de Planta

def opplantan_incompletos(request):
    opplantan = Operador_nacional_planta.objects.all()
    return render(request, 'Base_datos/opplanta_incompletos.html', {'opplantan' : opplantan} )

class CrearOperadordePlanta(CreateView):
    model = Operador_nacional_planta
    success_url = reverse_lazy('operadores_nacionales')
    fields = '__all__'

class ListarOperadordePlanta(ListView):
    model = Operador_nacional_planta
    fields = (Operador_nacional_planta.apellido, Operador_nacional_planta.nombre, Operador_nacional_planta.DNI, Operador_nacional_planta.habilitación, Operador_nacional_planta.instituto,
              Operador_nacional_planta.año_expediente, Operador_nacional_planta.número_expediente, Operador_nacional_planta.año_disposición, Operador_nacional_planta.número_disposición)

class VerOperadordePlanta(DetailView):
    model = Operador_nacional_planta

class ActualizarOPPlanta(UpdateView):
    model = Operador_nacional_planta
    success_url = reverse_lazy('operadores_nacionales')
    fields = '__all__'
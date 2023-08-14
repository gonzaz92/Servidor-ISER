from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from Base_datos.models import (Locutor_nacional, Locutor_local, Operador_nacional_radio, Operador_nacional_tv, Operador_nacional_planta,
                            Operador_local_radio, Operador_local_tv, Operador_local_planta, Productor, Guionista)
from django.urls import reverse_lazy
from django.db.models import Q
from Base_datos.forms import UsuarioForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator

@login_required
def index(request):
    return render(request, 'Base_datos/index.html')

@login_required
def buscar(request):
    query = request.GET.get('q')
    resultados_ln = Locutor_nacional.objects.filter(Q(apellido__icontains=query) | Q(nombre__icontains=query) | Q(DNI__icontains=query))
    resultados_ll = Locutor_local.objects.filter(Q(apellido__icontains=query) | Q(nombre__icontains=query) | Q(DNI__icontains=query))
    resultados_oprn = Operador_nacional_radio.objects.filter(Q(apellido__icontains=query) | Q(nombre__icontains=query) | Q(DNI__icontains=query))
    resultados_optvn = Operador_nacional_tv.objects.filter(Q(apellido__icontains=query) | Q(nombre__icontains=query) | Q(DNI__icontains=query))
    resultados_opplantan = Operador_nacional_planta.objects.filter(Q(apellido__icontains=query) | Q(nombre__icontains=query) | Q(DNI__icontains=query))
    resultados_oprl = Operador_local_radio.objects.filter(Q(apellido__icontains=query) | Q(nombre__icontains=query) | Q(DNI__icontains=query))
    resultados_optvl = Operador_local_tv.objects.filter(Q(apellido__icontains=query) | Q(nombre__icontains=query) | Q(DNI__icontains=query))
    resultados_opplantal = Operador_local_planta.objects.filter(Q(apellido__icontains=query) | Q(nombre__icontains=query) | Q(DNI__icontains=query))
    resultados_prod = Productor.objects.filter(Q(apellido__icontains=query) | Q(nombre__icontains=query) | Q(DNI__icontains=query))
    resultado_guion = Guionista.objects.filter(Q(apellido__icontains=query) | Q(nombre__icontains=query) | Q(DNI__icontains=query))
    resultados = (list(resultados_ln) + list(resultados_ll) + list(resultados_oprn) + list(resultados_optvn) + list(resultados_opplantan) +
                list(resultados_oprl) + list(resultados_optvl) + list(resultados_opplantal) + list(resultados_prod) + list(resultado_guion))
    return render(request, 'Base_datos/resultados_busqueda.html', {'resultados':resultados})

class UserSingUp(CreateView):
    form_class = UsuarioForm
    template_name = 'registration/singup.html'
    success_url = reverse_lazy('index')

class UserLogin(LoginView):
    success_url = reverse_lazy('index')

class UserLogout(LogoutView):
    next_page = reverse_lazy('index')

class ChangePassword(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('index')

############################################################# Locutores Nacionales ######################################################################

@login_required
def locutores(request):
    return render(request, 'Base_datos/locutores_nacionales.html')

@login_required
def ln_completos(request):
    lnc = Locutor_nacional.objects.all()
    return render(request, 'Base_datos/locutor_nacional_completos.html', {'lnc' : lnc})

@login_required
def ln_incompletos(request):
    ln = Locutor_nacional.objects.all()
    return render(request, 'Base_datos/ln_incompletos.html', {'ln' : ln})

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(lambda u: u.groups.filter(name='Registro').exists()), name='get')
class CrearLocutorNacional(CreateView):
    model = Locutor_nacional
    success_url = reverse_lazy('locutores_nacionales')
    fields = '__all__'

@method_decorator(login_required, name='get')
class ListarLocutorNacional(ListView):
    model = Locutor_nacional
    fields = (Locutor_nacional.apellido, Locutor_nacional.nombre, Locutor_nacional.DNI, Locutor_nacional.habilitación, Locutor_nacional.instituto,
            Locutor_nacional.año_expediente, Locutor_nacional.número_expediente,Locutor_nacional.año_disposición, Locutor_nacional.número_disposición)

@method_decorator(login_required, name='get')
class VerLocutorNacional(DetailView):
    model = Locutor_nacional

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(lambda u: u.groups.filter(name='Registro').exists()), name='get')
class ActualizarLN(UpdateView):
    model = Locutor_nacional
    success_url = reverse_lazy('locutores_nacionales')
    fields = '__all__'

############################################################# Locutores Locales ######################################################################

@login_required
def locutor_local(request):
    return render(request, 'Base_datos/locutores_locales.html')

@login_required
def ll_completos(request):
    llc = Locutor_local.objects.all()
    return render(request, 'Base_datos/locutor_local_completos.html', {'llc' : llc})

@login_required
def ll_incompletos(request):
    ll = Locutor_local.objects.all()
    return render(request, 'Base_datos/ll_incompletos.html', {'ll' : ll} )

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(lambda u: u.groups.filter(name='Registro').exists()), name='get')
class CrearLocutorLocal(CreateView):
    model = Locutor_local
    success_url = reverse_lazy('locutores_locales')
    fields = '__all__'

@method_decorator(login_required, name='get')
class ListarLocutorLocal(ListView):
    model = Locutor_local
    fields = (Locutor_local.apellido, Locutor_local.nombre, Locutor_local.DNI, Locutor_local.habilitación, Locutor_local.localidad, Locutor_local.provincia,
            Locutor_local.año_expediente, Locutor_local.número_expediente,Locutor_local.año_disposición, Locutor_local.número_disposición)

@method_decorator(login_required, name='get')
class VerLocutorLocal(DetailView):
    model = Locutor_local

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(lambda u: u.groups.filter(name='Registro').exists()), name='get')
class ActualizarLL(UpdateView):
    model = Locutor_local
    success_url = reverse_lazy('locutores_locales')
    fields = '__all__'

############################################################# Operadores Nacionales ######################################################################

@login_required
def operadores_nacionales(request):
    return render(request, 'Base_datos/operadores_nacionales.html')

############################################################# Operadores de Radio ######################################################################

@login_required
def oprn_completos(request):
    oprnc = Operador_nacional_radio.objects.all()
    return render(request, 'Base_datos/operador_nacional_radio_completos.html', {'oprnc' : oprnc})

@login_required
def oprn_incompletos(request):
    oprn = Operador_nacional_radio.objects.all()
    return render(request, 'Base_datos/oprn_incompletos.html', {'oprn' : oprn} )

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(lambda u: u.groups.filter(name='Registro').exists()), name='get')
class CrearOperadordeRadio(CreateView):
    model = Operador_nacional_radio
    success_url = reverse_lazy('operadores_nacionales')
    fields = '__all__'

@method_decorator(login_required, name='get')
class ListarOperadordeRadio(ListView):
    model = Operador_nacional_radio
    fields = (Operador_nacional_radio.apellido, Operador_nacional_radio.nombre, Operador_nacional_radio.DNI, Operador_nacional_radio.habilitación, Operador_nacional_radio.instituto,
            Operador_nacional_radio.año_expediente, Operador_nacional_radio.número_expediente, Operador_nacional_radio.año_disposición, Operador_nacional_radio.número_disposición)

@method_decorator(login_required, name='get')
class VerOperadordeRadio(DetailView):
    model = Operador_nacional_radio

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(lambda u: u.groups.filter(name='Registro').exists()), name='get')
class ActualizarOPR(UpdateView):
    model = Operador_nacional_radio
    success_url = reverse_lazy('operadores_nacionales')
    fields = '__all__'

############################################################# Operadores de TV ######################################################################

@login_required
def optvn_completos(request):
    optvnc = Operador_nacional_tv.objects.all()
    return render(request, 'Base_datos/operador_nacional_tv_completos.html', {'optvc' : optvnc})

@login_required
def optvn_incompletos(request):
    optvn = Operador_nacional_tv.objects.all()
    return render(request, 'Base_datos/optvn_incompletos.html', {'optvn' : optvn} )

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(lambda u: u.groups.filter(name='Registro').exists()), name='get')
class CrearOperadordeTV(CreateView):
    model = Operador_nacional_tv
    success_url = reverse_lazy('operadores_nacionales')
    fields = '__all__'

@method_decorator(login_required, name='get')
class ListarOperadordeTV(ListView):
    model = Operador_nacional_tv
    fields = (Operador_nacional_tv.apellido, Operador_nacional_tv.nombre, Operador_nacional_tv.DNI, Operador_nacional_tv.habilitación, Operador_nacional_tv.instituto,
            Operador_nacional_tv.año_expediente, Operador_nacional_tv.número_expediente, Operador_nacional_tv.año_disposición, Operador_nacional_tv.número_disposición)

@method_decorator(login_required, name='get')
class VerOperadordeTV(DetailView):
    model = Operador_nacional_tv

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(lambda u: u.groups.filter(name='Registro').exists()), name='get')
class ActualizarOPTV(UpdateView):
    model = Operador_nacional_tv
    success_url = reverse_lazy('operadores_nacionales')
    fields = '__all__'

############################################################# Operadores de Planta ######################################################################

@login_required
def opplantan_completos(request):
    opplantanc = Operador_nacional_planta.objects.all()
    return render(request, 'Base_datos/operador_nacional_planta_completos.html', {'opplantanc' : opplantanc})

@login_required
def opplantan_incompletos(request):
    opplantan = Operador_nacional_planta.objects.all()
    return render(request, 'Base_datos/opplantan_incompletos.html', {'opplantan' : opplantan} )

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(lambda u: u.groups.filter(name='Registro').exists()), name='get')
class CrearOperadordePlanta(CreateView):
    model = Operador_nacional_planta
    success_url = reverse_lazy('operadores_nacionales')
    fields = '__all__'

@method_decorator(login_required, name='get')
class ListarOperadordePlanta(ListView):
    model = Operador_nacional_planta
    fields = (Operador_nacional_planta.apellido, Operador_nacional_planta.nombre, Operador_nacional_planta.DNI, Operador_nacional_planta.habilitación, Operador_nacional_planta.instituto,
            Operador_nacional_planta.año_expediente, Operador_nacional_planta.número_expediente, Operador_nacional_planta.año_disposición, Operador_nacional_planta.número_disposición)

@method_decorator(login_required, name='get')
class VerOperadordePlanta(DetailView):
    model = Operador_nacional_planta

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(lambda u: u.groups.filter(name='Registro').exists()), name='get')
class ActualizarOPPlanta(UpdateView):
    model = Operador_nacional_planta
    success_url = reverse_lazy('operadores_nacionales')
    fields = '__all__'

############################################################# Operadores Locales ######################################################################

@login_required
def operadores_locales(request):
    return render(request, 'Base_datos/operadores_locales.html')

############################################################# Operadores de Radio ######################################################################

@login_required
def oprl_completos(request):
    oprlc = Operador_local_radio.objects.all()
    return render(request, 'Base_datos/operador_local_radio_completos.html', {'oprlc' : oprlc})

@login_required
def oprl_incompletos(request):
    oprl = Operador_local_radio.objects.all()
    return render(request, 'Base_datos/oprl_incompletos.html', {'oprl' : oprl} )

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(lambda u: u.groups.filter(name='Registro').exists()), name='get')
class CrearOperadordeRadioLocal(CreateView):
    model = Operador_local_radio
    success_url = reverse_lazy('operadores_locales')
    fields = '__all__'

@method_decorator(login_required, name='get')
class ListarOperadordeRadioLocal(ListView):
    model = Operador_local_radio
    fields = (Operador_local_radio.apellido, Operador_local_radio.nombre, Operador_local_radio.DNI, Operador_local_radio.habilitación,
            Operador_local_radio.año_expediente, Operador_local_radio.número_expediente, Operador_local_radio.año_disposición, Operador_local_radio.número_disposición)

@method_decorator(login_required, name='get')
class VerOperadordeRadioLocal(DetailView):
    model = Operador_local_radio

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(lambda u: u.groups.filter(name='Registro').exists()), name='get')
class ActualizarOPRLocal(UpdateView):
    model = Operador_local_radio
    success_url = reverse_lazy('operadores_locales')
    fields = '__all__'

############################################################# Operadores de TV ######################################################################

@login_required
def optvl_completos(request):
    optvlc = Operador_local_tv.objects.all()
    return render(request, 'Base_datos/operador_local_tv_completos.html', {'optvlc' : optvlc})

@login_required
def optvl_incompletos(request):
    optvl = Operador_local_tv.objects.all()
    return render(request, 'Base_datos/optvl_incompletos.html', {'optvl' : optvl} )

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(lambda u: u.groups.filter(name='Registro').exists()), name='get')
class CrearOperadordeTVLocal(CreateView):
    model = Operador_local_tv
    success_url = reverse_lazy('operadores_locales')
    fields = '__all__'

@method_decorator(login_required, name='get')
class ListarOperadordeTVLocal(ListView):
    model = Operador_local_tv
    fields = (Operador_local_tv.apellido, Operador_local_tv.nombre, Operador_local_tv.DNI, Operador_local_tv.habilitación,
            Operador_local_tv.año_expediente, Operador_local_tv.número_expediente, Operador_local_tv.año_disposición, Operador_local_tv.número_disposición)

@method_decorator(login_required, name='get')
class VerOperadordeTVLocal(DetailView):
    model = Operador_local_tv

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(lambda u: u.groups.filter(name='Registro').exists()), name='get')
class ActualizarOPTVLocal(UpdateView):
    model = Operador_local_tv
    success_url = reverse_lazy('operadores_locales')
    fields = '__all__'

############################################################# Operadores de Planta ######################################################################

@login_required
def opplantal_completos(request):
    opplantalc = Operador_local_planta.objects.all()
    return render(request, 'Base_datos/operador_local_planta_completos.html', {'opplantalc' : opplantalc})

@login_required
def opplantal_incompletos(request):
    opplantal = Operador_local_planta.objects.all()
    return render(request, 'Base_datos/opplantal_incompletos.html', {'opplantal' : opplantal} )

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(lambda u: u.groups.filter(name='Registro').exists()), name='get')
class CrearOperadordePlantaLocal(CreateView):
    model = Operador_local_planta
    success_url = reverse_lazy('operadores_locales')
    fields = '__all__'

@method_decorator(login_required, name='get')
class ListarOperadordePlantaLocal(ListView):
    model = Operador_local_planta
    fields = (Operador_local_planta.apellido, Operador_local_planta.nombre, Operador_local_planta.DNI, Operador_local_planta.habilitación,
            Operador_local_planta.año_expediente, Operador_local_planta.número_expediente, Operador_local_planta.año_disposición, Operador_local_planta.número_disposición)

@method_decorator(login_required, name='get')
class VerOperadordePlantaLocal(DetailView):
    model = Operador_local_planta

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(lambda u: u.groups.filter(name='Registro').exists()), name='get')
class ActualizarOPPlantaLocal(UpdateView):
    model = Operador_local_planta
    success_url = reverse_lazy('operadores_locales')
    fields = '__all__'

############################################################# Productores y Directores ######################################################################

@login_required
def productores(request):
    return render(request, 'Base_datos/productores_y_directores.html')

@login_required
def prod_completos(request):
    prodc = Productor.objects.all()
    return render(request, 'Base_datos/productores_completos.html', {'prodc' : prodc})

def prod_incompletos(request):
    prod = Productor.objects.all()
    return render(request, 'Base_datos/prod_incompletos.html', {'prod' : prod} )

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(lambda u: u.groups.filter(name='Registro').exists()), name='get')
class CrearProductor(CreateView):
    model = Productor
    success_url = reverse_lazy('productores_y_directores')
    fields = '__all__'

@method_decorator(login_required, name='get')
class ListarProductor(ListView):
    model = Productor
    fields = (Productor.apellido, Productor.nombre, Productor.DNI, Productor.habilitación, Productor.instituto,
            Productor.año_expediente, Productor.número_expediente, Productor.año_disposición, Productor.número_disposición)

@method_decorator(login_required, name='get')
class VerProductor(DetailView):
    model = Productor

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(lambda u: u.groups.filter(name='Registro').exists()), name='get')
class ActualizarProd(UpdateView):
    model = Productor
    success_url = reverse_lazy('productores_y_directores')
    fields = '__all__'

############################################################# Guionistas ######################################################################

@login_required
def guionistas(request):
    return render(request, 'Base_datos/guionistas.html')

@login_required
def guion_completos(request):
    guionc = Guionista.objects.all()
    return render(request, 'Base_datos/guionistas_completos.html', {'guionc' : guionc})

@login_required
def guion_incompletos(request):
    guion = Guionista.objects.all()
    return render(request, 'Base_datos/guion_incompletos.html', {'guion' : guion} )

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(lambda u: u.groups.filter(name='Registro').exists()), name='get')
class CrearGuionista(CreateView):
    model = Guionista
    success_url = reverse_lazy('guionistas')
    fields = '__all__'

@method_decorator(login_required, name='get')
class ListarGuionista(ListView):
    model = Guionista
    fields = (Guionista.apellido, Guionista.nombre, Guionista.DNI, Guionista.habilitación, Guionista.instituto,
            Guionista.año_expediente, Guionista.número_expediente, Guionista.año_disposición, Guionista.número_disposición)

@method_decorator(login_required, name='get')
class VerGuionista(DetailView):
    model = Guionista

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(lambda u: u.groups.filter(name='Registro').exists()), name='get')
class ActualizarGuion(UpdateView):
    model = Guionista
    success_url = reverse_lazy('guionistas')
    fields = '__all__'
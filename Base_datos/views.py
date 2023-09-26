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

# Permisos Locutor Nacional

def carga_LocutorNacional(user):
    return user.has_perm('Base_datos.add_locutor_nacional')

def actualizar_LocutorNacional(user):
    return user.has_perm('Base_datos.change_locutor_nacional')

def ver_LocutorNacional(user):
    return user.has_perm('Base_datos.view_locutor_nacional')

# Permisos Locutor Local

def carga_LocutorLocal(user):
    return user.has_perm('Base_datos.add_locutor_local')

def actualizar_LocutorLocal(user):
    return user.has_perm('Base_datos.change_locutor_local')

def ver_LocutorLocal(user):
    return user.has_perm('Base_datos.view_locutor_local')

# Permisos Operador Nacional de Radio

def carga_OperadorNRadio(user):
    return user.has_perm('Base_datos.add_operador_nacional_radio')

def actualizar_OperadorNRadio(user):
    return user.has_perm('Base_datos.change_operador_nacional_radio')

def ver_OperadorNRadio(user):
    return user.has_perm('Base_datos.view_operador_nacional_radio')

# Permisos Operador Nacional de TV

def carga_OperadorNTV(user):
    return user.has_perm('Base_datos.add_operador_nacional_tv')

def actualizar_OperadorNTV(user):
    return user.has_perm('Base_datos.change_operador_nacional_tv')

def ver_OperadorNTV(user):
    return user.has_perm('Base_datos.view_operador_nacional_tv')

# Permisos Operador Nacional de Planta Transmisora

def carga_OperadorNPlanta(user):
    return user.has_perm('Base_datos.add_operador_nacional_planta')

def actualizar_OperadorNPlanta(user):
    return user.has_perm('Base_datos.change_operador_nacional_planta')

def ver_OperadorNPlanta(user):
    return user.has_perm('Base_datos.view_operador_nacional_planta')

# Permisos Operador Local de Radio

def carga_OperadorLRadio(user):
    return user.has_perm('Base_datos.add_operador_local_radio')

def actualizar_OperadorLRadio(user):
    return user.has_perm('Base_datos.change_operador_local_radio')

def ver_OperadorLRadio(user):
    return user.has_perm('Base_datos.view_operador_local_radio')

# Permisos Operador Local de TV

def carga_OperadorLTV(user):
    return user.has_perm('Base_datos.add_operador_local_tv')

def actualizar_OperadorLTV(user):
    return user.has_perm('Base_datos.change_operador_local_tv')

def ver_OperadorLTV(user):
    return user.has_perm('Base_datos.view_operador_local_tv')

# Permisos Operador Local de Planta Transmisora

def carga_OperadorLPlanta(user):
    return user.has_perm('Base_datos.add_operador_local_planta')

def actualizar_OperadorLPlanta(user):
    return user.has_perm('Base_datos.change_operador_local_planta')

def ver_OperadorLPlanta(user):
    return user.has_perm('Base_datos.view_operador_local_planta')

# Permiso de Productores

def carga_productor(user):
    return user.has_perm('Base_datos.add_productor')

def actualizar_productor(user):
    return user.has_perm('Base_datos.chage_productor')

def ver_productor(user):
    return user.has_perm('Base_datos.view_productor')

# Permisos de Guionistas

def carga_guionista(user):
    return user.has_perm('Base_datos.add_guionista')

def actualizar_guionista(user):
    return user.has_perm('Base_datos.change_guionista')

def ver_guionista(user):
    return user.has_perm('Base_datos.view_guionista')

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
@user_passes_test(ver_LocutorNacional)
def ln_completos(request):
    lnc = Locutor_nacional.objects.all()
    return render(request, 'Base_datos/locutor_nacional_completos.html', {'lnc' : lnc})

@login_required
@user_passes_test(ver_LocutorNacional)
def ln_completos_exp(request):
    lnc_exp = Locutor_nacional.objects.all()
    return render(request, 'Base_datos/locutor_nacional_completos_exp.html', {'lnc_exp' : lnc_exp})

@login_required
@user_passes_test(ver_LocutorNacional)
def ln_incompletos(request):
    ln = Locutor_nacional.objects.all()
    return render(request, 'Base_datos/ln_incompletos.html', {'ln' : ln})

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(carga_LocutorNacional), name='get')
class CrearLocutorNacional(CreateView):
    model = Locutor_nacional
    success_url = reverse_lazy('locutores_nacionales')
    fields = '__all__'

@method_decorator(login_required, name='get')
class ListarLocutorNacional(ListView):
    model = Locutor_nacional
    fields = (Locutor_nacional.apellido, Locutor_nacional.nombre, Locutor_nacional.DNI, Locutor_nacional.habilitación, Locutor_nacional.instituto,
            Locutor_nacional.año_expediente, Locutor_nacional.número_expediente,Locutor_nacional.año_disposición, Locutor_nacional.número_disposición)
    
    def get_queryset(self):
        return Locutor_nacional.objects.all().order_by('-habilitación')

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(ver_LocutorNacional), name='get')
class VerLocutorNacional(DetailView):
    model = Locutor_nacional

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(actualizar_LocutorNacional), name='get')
class ActualizarLN(UpdateView):
    model = Locutor_nacional
    success_url = reverse_lazy('locutores_nacionales')
    fields = '__all__'

############################################################# Locutores Locales ######################################################################

@login_required
def locutor_local(request):
    return render(request, 'Base_datos/locutores_locales.html')

@login_required
@user_passes_test(ver_LocutorLocal)
def ll_completos(request):
    llc = Locutor_local.objects.all()
    return render(request, 'Base_datos/locutor_local_completos.html', {'llc' : llc})

@login_required
@user_passes_test(ver_LocutorLocal)
def ll_completos_exp(request):
    llc_exp = Locutor_local.objects.all()
    return render(request, 'Base_datos/locutor_local_completos_exp.html', {'llc_exp' : llc_exp})

@login_required
@user_passes_test(ver_LocutorLocal)
def ll_incompletos(request):
    ll = Locutor_local.objects.all()
    return render(request, 'Base_datos/ll_incompletos.html', {'ll' : ll} )

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(carga_LocutorLocal), name='get')
class CrearLocutorLocal(CreateView):
    model = Locutor_local
    success_url = reverse_lazy('locutores_locales')
    fields = '__all__'

@method_decorator(login_required, name='get')
class ListarLocutorLocal(ListView):
    model = Locutor_local
    fields = (Locutor_local.apellido, Locutor_local.nombre, Locutor_local.DNI, Locutor_local.habilitación, Locutor_local.localidad, Locutor_local.provincia,
            Locutor_local.año_expediente, Locutor_local.número_expediente,Locutor_local.año_disposición, Locutor_local.número_disposición)
    
    def get_queryset(self):
        return Locutor_local.objects.all().order_by('-habilitación')

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(ver_LocutorLocal), name='get')
class VerLocutorLocal(DetailView):
    model = Locutor_local

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(actualizar_LocutorLocal), name='get')
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
@user_passes_test(ver_OperadorNRadio)
def oprn_completos(request):
    oprnc = Operador_nacional_radio.objects.all()
    return render(request, 'Base_datos/operador_nacional_radio_completos.html', {'oprnc' : oprnc})

@login_required
@user_passes_test(ver_OperadorNRadio)
def oprn_completos_exp(request):
    oprnc_exp = Operador_nacional_radio.objects.all()
    return render(request, 'Base_datos/operador_nacional_radio_completos_exp.html', {'oprnc_exp' : oprnc_exp})

@login_required
@user_passes_test(ver_OperadorNRadio)
def oprn_incompletos(request):
    oprn = Operador_nacional_radio.objects.all()
    return render(request, 'Base_datos/oprn_incompletos.html', {'oprn' : oprn} )

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(carga_OperadorNRadio), name='get')
class CrearOperadordeRadio(CreateView):
    model = Operador_nacional_radio
    success_url = reverse_lazy('operadores_nacionales')
    fields = '__all__'

@method_decorator(login_required, name='get')
class ListarOperadordeRadio(ListView):
    model = Operador_nacional_radio
    fields = (Operador_nacional_radio.apellido, Operador_nacional_radio.nombre, Operador_nacional_radio.DNI, Operador_nacional_radio.habilitación, Operador_nacional_radio.instituto,
            Operador_nacional_radio.año_expediente, Operador_nacional_radio.número_expediente, Operador_nacional_radio.año_disposición, Operador_nacional_radio.número_disposición)
    
    def get_queryset(self):
        return Operador_nacional_radio.objects.all().order_by('-habilitación')

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(ver_OperadorNRadio), name='get')
class VerOperadordeRadio(DetailView):
    model = Operador_nacional_radio

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(actualizar_OperadorNRadio), name='get')
class ActualizarOPR(UpdateView):
    model = Operador_nacional_radio
    success_url = reverse_lazy('operadores_nacionales')
    fields = '__all__'

############################################################# Operadores de TV ######################################################################

@login_required
@user_passes_test(ver_OperadorNTV)
def optvn_completos(request):
    optvnc = Operador_nacional_tv.objects.all()
    return render(request, 'Base_datos/operador_nacional_tv_completos.html', {'optvnc' : optvnc})

@login_required
@user_passes_test(ver_OperadorNTV)
def optvn_completos_exp(request):
    optvnc_exp = Operador_nacional_tv.objects.all()
    return render(request, 'Base_datos/operador_nacional_tv_completos_exp.html', {'optvnc_exp' : optvnc_exp})

@login_required
@user_passes_test(ver_OperadorNTV)
def optvn_incompletos(request):
    optvn = Operador_nacional_tv.objects.all()
    return render(request, 'Base_datos/optvn_incompletos.html', {'optvn' : optvn} )

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(carga_OperadorNTV), name='get')
class CrearOperadordeTV(CreateView):
    model = Operador_nacional_tv
    success_url = reverse_lazy('operadores_nacionales')
    fields = '__all__'

@method_decorator(login_required, name='get')
class ListarOperadordeTV(ListView):
    model = Operador_nacional_tv
    fields = (Operador_nacional_tv.apellido, Operador_nacional_tv.nombre, Operador_nacional_tv.DNI, Operador_nacional_tv.habilitación, Operador_nacional_tv.instituto,
            Operador_nacional_tv.año_expediente, Operador_nacional_tv.número_expediente, Operador_nacional_tv.año_disposición, Operador_nacional_tv.número_disposición)
    
    def get_queryset(self):
        return Operador_nacional_tv.objects.all().order_by('-habilitación')

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(ver_OperadorNTV), name='get')
class VerOperadordeTV(DetailView):
    model = Operador_nacional_tv

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(actualizar_OperadorNTV), name='get')
class ActualizarOPTV(UpdateView):
    model = Operador_nacional_tv
    success_url = reverse_lazy('operadores_nacionales')
    fields = '__all__'

############################################################# Operadores de Planta ######################################################################

@login_required
@user_passes_test(ver_OperadorNPlanta)
def opplantan_completos(request):
    opplantanc = Operador_nacional_planta.objects.all()
    return render(request, 'Base_datos/operador_nacional_planta_completos.html', {'opplantanc' : opplantanc})

@login_required
@user_passes_test(ver_OperadorNPlanta)
def opplantan_completos_exp(request):
    opplantanc_exp = Operador_nacional_planta.objects.all()
    return render(request, 'Base_datos/operador_nacional_planta_completos_exp.html', {'opplantanc_exp' : opplantanc_exp})

@login_required
@user_passes_test(ver_OperadorNPlanta)
def opplantan_incompletos(request):
    opplantan = Operador_nacional_planta.objects.all()
    return render(request, 'Base_datos/opplantan_incompletos.html', {'opplantan' : opplantan} )

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(carga_OperadorNPlanta), name='get')
class CrearOperadordePlanta(CreateView):
    model = Operador_nacional_planta
    success_url = reverse_lazy('operadores_nacionales')
    fields = '__all__'

@method_decorator(login_required, name='get')
class ListarOperadordePlanta(ListView):
    model = Operador_nacional_planta
    fields = (Operador_nacional_planta.apellido, Operador_nacional_planta.nombre, Operador_nacional_planta.DNI, Operador_nacional_planta.habilitación, Operador_nacional_planta.instituto,
            Operador_nacional_planta.año_expediente, Operador_nacional_planta.número_expediente, Operador_nacional_planta.año_disposición, Operador_nacional_planta.número_disposición)
    
    def get_queryset(self):
        return Operador_nacional_planta.objects.all().order_by('-habilitación')

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(ver_OperadorNPlanta), name='get')
class VerOperadordePlanta(DetailView):
    model = Operador_nacional_planta

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(actualizar_OperadorNPlanta), name='get')
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
@user_passes_test(ver_OperadorLRadio)
def oprl_completos(request):
    oprlc = Operador_local_radio.objects.all()
    return render(request, 'Base_datos/operador_local_radio_completos.html', {'oprlc' : oprlc})

@login_required
@user_passes_test(ver_OperadorLRadio)
def oprl_completos_exp(request):
    oprlc_exp = Operador_local_radio.objects.all()
    return render(request, 'Base_datos/operador_local_radio_completos_exp.html', {'oprlc_exp' : oprlc_exp})

@login_required
@user_passes_test(ver_OperadorLRadio)
def oprl_incompletos(request):
    oprl = Operador_local_radio.objects.all()
    return render(request, 'Base_datos/oprl_incompletos.html', {'oprl' : oprl} )

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(carga_OperadorLRadio), name='get')
class CrearOperadordeRadioLocal(CreateView):
    model = Operador_local_radio
    success_url = reverse_lazy('operadores_locales')
    fields = '__all__'

@method_decorator(login_required, name='get')
class ListarOperadordeRadioLocal(ListView):
    model = Operador_local_radio
    fields = (Operador_local_radio.apellido, Operador_local_radio.nombre, Operador_local_radio.DNI, Operador_local_radio.habilitación,
            Operador_local_radio.año_expediente, Operador_local_radio.número_expediente, Operador_local_radio.año_disposición, Operador_local_radio.número_disposición)
    
    def get_queryset(self):
        return Operador_local_radio.objects.all().order_by('-habilitación')

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(ver_OperadorLRadio), name='get')
class VerOperadordeRadioLocal(DetailView):
    model = Operador_local_radio

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(ver_OperadorLRadio), name='get')
class ActualizarOPRLocal(UpdateView):
    model = Operador_local_radio
    success_url = reverse_lazy('operadores_locales')
    fields = '__all__'

############################################################# Operadores de TV ######################################################################

@login_required
@user_passes_test(ver_OperadorLTV)
def optvl_completos(request):
    optvlc = Operador_local_tv.objects.all()
    return render(request, 'Base_datos/operador_local_tv_completos.html', {'optvlc' : optvlc})

@login_required
@user_passes_test(ver_OperadorLTV)
def optvl_completos_exp(request):
    optvlc_exp = Operador_local_tv.objects.all()
    return render(request, 'Base_datos/operador_local_tv_completos_exp.html', {'optvlc_exp' : optvlc_exp})

@login_required
@user_passes_test(ver_OperadorLTV)
def optvl_incompletos(request):
    optvl = Operador_local_tv.objects.all()
    return render(request, 'Base_datos/optvl_incompletos.html', {'optvl' : optvl} )

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(carga_OperadorLTV), name='get')
class CrearOperadordeTVLocal(CreateView):
    model = Operador_local_tv
    success_url = reverse_lazy('operadores_locales')
    fields = '__all__'

@method_decorator(login_required, name='get')
class ListarOperadordeTVLocal(ListView):
    model = Operador_local_tv
    fields = (Operador_local_tv.apellido, Operador_local_tv.nombre, Operador_local_tv.DNI, Operador_local_tv.habilitación,
            Operador_local_tv.año_expediente, Operador_local_tv.número_expediente, Operador_local_tv.año_disposición, Operador_local_tv.número_disposición)
    
    def get_queryset(self):
        return Operador_local_tv.objects.all().order_by('-habilitación')

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(ver_OperadorLTV), name='get')
class VerOperadordeTVLocal(DetailView):
    model = Operador_local_tv

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(actualizar_OperadorLTV), name='get')
class ActualizarOPTVLocal(UpdateView):
    model = Operador_local_tv
    success_url = reverse_lazy('operadores_locales')
    fields = '__all__'

############################################################# Operadores de Planta ######################################################################

@login_required
@user_passes_test(ver_OperadorLPlanta)
def opplantal_completos(request):
    opplantalc = Operador_local_planta.objects.all()
    return render(request, 'Base_datos/operador_local_planta_completos.html', {'opplantalc' : opplantalc})

@login_required
@user_passes_test(ver_OperadorLPlanta)
def opplantal_completos_exp(request):
    opplantalc_exp = Operador_local_planta.objects.all()
    return render(request, 'Base_datos/operador_local_planta_completos_exp.html', {'opplantalc_exp' : opplantalc_exp})

@login_required
@user_passes_test(ver_OperadorLPlanta)
def opplantal_incompletos(request):
    opplantal = Operador_local_planta.objects.all()
    return render(request, 'Base_datos/opplantal_incompletos.html', {'opplantal' : opplantal} )

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(carga_OperadorLPlanta), name='get')
class CrearOperadordePlantaLocal(CreateView):
    model = Operador_local_planta
    success_url = reverse_lazy('operadores_locales')
    fields = '__all__'

@method_decorator(login_required, name='get')
class ListarOperadordePlantaLocal(ListView):
    model = Operador_local_planta
    fields = (Operador_local_planta.apellido, Operador_local_planta.nombre, Operador_local_planta.DNI, Operador_local_planta.habilitación,
            Operador_local_planta.año_expediente, Operador_local_planta.número_expediente, Operador_local_planta.año_disposición, Operador_local_planta.número_disposición)
    
    def get_queryset(self):
        return Operador_local_planta.objects.all().order_by('-habilitación')

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(ver_OperadorLPlanta), name='get')
class VerOperadordePlantaLocal(DetailView):
    model = Operador_local_planta

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(actualizar_OperadorLPlanta), name='get')
class ActualizarOPPlantaLocal(UpdateView):
    model = Operador_local_planta
    success_url = reverse_lazy('operadores_locales')
    fields = '__all__'

############################################################# Productores y Directores ######################################################################

@login_required
def productores(request):
    return render(request, 'Base_datos/productores_y_directores.html')

@login_required
@user_passes_test(ver_productor)
def prod_completos(request):
    prodc = Productor.objects.all()
    return render(request, 'Base_datos/productores_completos.html', {'prodc' : prodc})

@login_required
@user_passes_test(ver_productor)
def prod_completos_exp(request):
    prodc_exp = Productor.objects.all()
    return render(request, 'Base_datos/productores_completos_exp.html', {'prodc_exp' : prodc_exp})

@login_required
@user_passes_test(ver_productor)
def prod_incompletos(request):
    prod = Productor.objects.all()
    return render(request, 'Base_datos/prod_incompletos.html', {'prod' : prod} )

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(carga_productor), name='get')
class CrearProductor(CreateView):
    model = Productor
    success_url = reverse_lazy('productores_y_directores')
    fields = '__all__'

@method_decorator(login_required, name='get')
class ListarProductor(ListView):
    model = Productor
    fields = (Productor.apellido, Productor.nombre, Productor.DNI, Productor.habilitación, Productor.instituto,
            Productor.año_expediente, Productor.número_expediente, Productor.año_disposición, Productor.número_disposición)
    
    def get_queryset(self):
        return Productor.objects.all().order_by('-habilitación')

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(ver_productor), name='get')
class VerProductor(DetailView):
    model = Productor

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(actualizar_productor), name='get')
class ActualizarProd(UpdateView):
    model = Productor
    success_url = reverse_lazy('productores_y_directores')
    fields = '__all__'

############################################################# Guionistas ######################################################################

@login_required
def guionistas(request):
    return render(request, 'Base_datos/guionistas.html')

@login_required
@user_passes_test(ver_guionista)
def guion_completos(request):
    guionc = Guionista.objects.all()
    return render(request, 'Base_datos/guionistas_completos.html', {'guionc' : guionc})

@login_required
@user_passes_test(ver_guionista)
def guion_completos_exp(request):
    guionc_exp = Guionista.objects.all()
    return render(request, 'Base_datos/guionistas_completos_exp.html', {'guionc_exp' : guionc_exp})

@login_required
@user_passes_test(ver_guionista)
def guion_incompletos(request):
    guion = Guionista.objects.all()
    return render(request, 'Base_datos/guion_incompletos.html', {'guion' : guion} )

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(carga_guionista), name='get')
class CrearGuionista(CreateView):
    model = Guionista
    success_url = reverse_lazy('guionistas')
    fields = '__all__'

@method_decorator(login_required, name='get')
class ListarGuionista(ListView):
    model = Guionista
    fields = (Guionista.apellido, Guionista.nombre, Guionista.DNI, Guionista.habilitación, Guionista.instituto,
            Guionista.año_expediente, Guionista.número_expediente, Guionista.año_disposición, Guionista.número_disposición)
    
    def get_queryset(self):
        return Guionista.objects.all().order_by('-habilitación')

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(ver_guionista), name='get')
class VerGuionista(DetailView):
    model = Guionista

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(actualizar_guionista), name='get')
class ActualizarGuion(UpdateView):
    model = Guionista
    success_url = reverse_lazy('guionistas')
    fields = '__all__'
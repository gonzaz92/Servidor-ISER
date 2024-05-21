from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from Base_datos.models import (Locutor_nacional, Locutor_local, Operador_nacional_radio, Operador_nacional_tv, Operador_nacional_planta,
                            Operador_local_radio, Operador_local_tv, Operador_local_planta, Productor, Guionista)
from django.urls import reverse_lazy
from django.db.models import Q
from Base_datos.forms import (UsuarioForm,
                            LocutorNacionalForm, RadioNacionalForm, TVNacionalForm, PlantaNacionalForm,
                            LocutorLocalForm, RadioLocalForm, TVLocalForm, PlantaLocalForm,
                            ProductorForm, GuionistaForm)
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator
from datetime import datetime, timedelta

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

exp = Q(número_disposición__isnull=True) & Q(chequeo_expediente=True)

########################## Condiciones Nacional ############################

completos_nacional = Q(número_disposición__isnull=True) & Q(chequeo_expediente=False) & (
                                                                                        Q(chequeo_dni=True) &
                                                                                        Q(chequeo_formulario=True) &
                                                                                        Q(chequeo_secu=True) &
                                                                                        Q(chequeo_insti=True)
                                                                                        )

incompletos_nacional = Q(número_disposición__isnull=True) & Q(chequeo_expediente=False) & Q(
                                                                                            Q(chequeo_dni=False) |
                                                                                            Q(chequeo_formulario=False) |
                                                                                            Q(chequeo_secu=False) |
                                                                                            Q(chequeo_insti=False)
                                                                                            )

########################## Condiciones Local ############################

completos_local = Q(número_disposición__isnull=True) & Q(chequeo_expediente=False) & (
                                                                                    Q(chequeo_dni=True) &
                                                                                    Q(chequeo_formulario=True) &
                                                                                    Q(chequeo_secu=True) &
                                                                                    Q(chequeo_certi=True)
                                                                                    )

limite = datetime.now().date() - timedelta(days=10)

incompletos_local = Q(número_disposición__isnull=True) & Q(chequeo_expediente=False) & (Q(reclamo_tad__gte=limite) | Q(reclamo_tad__isnull=True)) & (
                                                                                                                                                    Q(chequeo_dni=False) |
                                                                                                                                                    Q(chequeo_formulario=False) |
                                                                                                                                                    Q(chequeo_secu=False) |
                                                                                                                                                    Q(chequeo_certi=False)
                                                                                                                                                    )

archivo_local = Q(número_disposición__isnull=True) & Q(chequeo_expediente=False) & Q(reclamo_tad__lt=limite) & (
                                                                                                                Q(chequeo_dni=False) |
                                                                                                                Q(chequeo_formulario=False) |
                                                                                                                Q(chequeo_secu=False) |
                                                                                                                Q(chequeo_certi=False)
                                                                                                                )

########################## Funciones para condición ############################

def pag_nacional(a, b, c):
    object = b.objects.filter(c).order_by('-id').all()
    paginator = Paginator(object, 100)
    page_number = a.GET.get('page')
    objetc_nacional = paginator.get_page(page_number)
    return objetc_nacional

def pag_local(a, b, c):
    object = b.objects.filter(c).order_by('-id').all()
    paginator = Paginator(object, 100)
    page_number = a.GET.get('page')
    objetc_local = paginator.get_page(page_number)
    return objetc_local

###################### Vistas ################################

@login_required
def index(request):
    return render(request, 'Base_datos/index.html')

@login_required
def buscar(request):
    query = request.GET.get('q')
    modelos = [
        Locutor_nacional, Locutor_local, Operador_nacional_radio, Operador_nacional_tv, Operador_nacional_planta,
        Operador_local_radio, Operador_local_tv, Operador_local_planta, Productor, Guionista
    ]
    resultados = []
    for modelo in modelos:
        busqueda = modelo.objects.filter(Q(apellido__icontains=query) | Q(nombre__icontains=query) | Q(DNI__icontains=query))
        resultados.extend(busqueda)
    return render(request, 'Base_datos/resultados_busqueda.html', {'resultados': resultados})

###################### Usuarios ################################

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
    lnc = pag_nacional(request, Locutor_nacional, completos_nacional)
    return render(request, 'Base_datos/locutor_nacional_completos.html', {'lnc' : lnc})

@login_required
@user_passes_test(ver_LocutorNacional)
def ln_completos_exp(request):
    lnc_exp = pag_nacional(request, Locutor_nacional, exp)
    return render(request, 'Base_datos/locutor_nacional_completos_exp.html', {'lnc_exp' : lnc_exp})

@login_required
@user_passes_test(ver_LocutorNacional)
def ln_incompletos(request):
    ln = pag_nacional(request, Locutor_nacional, incompletos_nacional)
    return render(request, 'Base_datos/ln_incompletos.html', {'ln': ln})

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(carga_LocutorNacional), name='get')
class CrearLocutorNacional(CreateView):
    template_name='Base_datos/locutor_nacional_form.html'
    form_class= LocutorNacionalForm
    success_url = reverse_lazy('locutores_nacionales')

@method_decorator(login_required, name='get')
class ListarLocutorNacional(ListView):
    model = Locutor_nacional
    fields = '__all__'
    
    def get_queryset(self):
        return Locutor_nacional.objects.all().order_by('-habilitación')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(context['object_list'], 100)
        page = self.request.GET.get('page')
        locutores_paginados = paginator.get_page(page)
        context['object_list'] = locutores_paginados
        return context

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(ver_LocutorNacional), name='get')
class VerLocutorNacional(DetailView):
    model = Locutor_nacional

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(actualizar_LocutorNacional), name='get')
class ActualizarLN(UpdateView):
    model = Locutor_nacional
    success_url = reverse_lazy('locutores_nacionales')
    form_class = LocutorNacionalForm

############################################################# Locutores Locales ######################################################################

@login_required
def locutor_local(request):
    return render(request, 'Base_datos/locutores_locales.html')

@login_required
@user_passes_test(ver_LocutorLocal)
def ll_completos(request):
    llc = pag_local(request, Locutor_local, completos_local)
    return render(request, 'Base_datos/locutor_local_completos.html', {'llc' : llc})

@login_required
@user_passes_test(ver_LocutorLocal)
def ll_completos_exp(request):
    llc_exp = pag_local(request, Locutor_local, exp)
    return render(request, 'Base_datos/locutor_local_completos_exp.html', {'llc_exp' : llc_exp})

@login_required
@user_passes_test(ver_LocutorLocal)
def ll_incompletos(request):
    ll = pag_local(request, Locutor_local, incompletos_local)
    return render(request, 'Base_datos/ll_incompletos.html', {'ll' : ll} )

@login_required
@user_passes_test(ver_LocutorLocal)
def ll_archivo(request):
    ll_arch = pag_local(request, Locutor_local, archivo_local)
    return render(request, 'Base_datos/ll_archivo.html', {'ll_arch' : ll_arch} )

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(carga_LocutorLocal), name='get')
class CrearLocutorLocal(CreateView):
    template_name='Base_datos/locutor_local_form.html'
    form_class= LocutorLocalForm
    success_url = reverse_lazy('locutores_locales')

@method_decorator(login_required, name='get')
class ListarLocutorLocal(ListView):
    model = Locutor_local
    fields = (Locutor_local.apellido, Locutor_local.nombre, Locutor_local.DNI, Locutor_local.habilitación, Locutor_local.localidad, Locutor_local.provincia,
            Locutor_local.año_expediente, Locutor_local.número_expediente,Locutor_local.año_disposición, Locutor_local.número_disposición)
    
    def get_queryset(self):
        return Locutor_local.objects.all().order_by('-habilitación')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(context['object_list'], 100)
        page = self.request.GET.get('page')
        locutores_paginados = paginator.get_page(page)
        context['object_list'] = locutores_paginados
        return context

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(ver_LocutorLocal), name='get')
class VerLocutorLocal(DetailView):
    model = Locutor_local

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(actualizar_LocutorLocal), name='get')
class ActualizarLL(UpdateView):
    model = Locutor_local
    success_url = reverse_lazy('locutores_locales')
    form_class = LocutorLocalForm

############################################################# Operadores Nacionales ######################################################################

@login_required
def operadores_nacionales(request):
    return render(request, 'Base_datos/operadores_nacionales.html')

############################################################# Operadores de Radio ######################################################################

@login_required
@user_passes_test(ver_OperadorNRadio)
def oprn_completos(request):
    oprnc = pag_nacional(request, Operador_nacional_radio, completos_nacional)
    return render(request, 'Base_datos/operador_nacional_radio_completos.html', {'oprnc' : oprnc})

@login_required
@user_passes_test(ver_OperadorNRadio)
def oprn_completos_exp(request):
    oprnc_exp = pag_nacional(request, Operador_nacional_radio, exp)
    return render(request, 'Base_datos/operador_nacional_radio_completos_exp.html', {'oprnc_exp' : oprnc_exp})

@login_required
@user_passes_test(ver_OperadorNRadio)
def oprn_incompletos(request):
    oprn = pag_nacional(request, Operador_nacional_radio, incompletos_nacional)
    return render(request, 'Base_datos/oprn_incompletos.html', {'oprn' : oprn} )

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(carga_OperadorNRadio), name='get')
class CrearOperadordeRadio(CreateView):
    template_name = 'Base_datos/operador_nacional_radio_form.html'
    form_class = RadioNacionalForm
    success_url = reverse_lazy('operadores_nacionales')

@method_decorator(login_required, name='get')
class ListarOperadordeRadio(ListView):
    model = Operador_nacional_radio
    fields = (Operador_nacional_radio.apellido, Operador_nacional_radio.nombre, Operador_nacional_radio.DNI, Operador_nacional_radio.habilitación, Operador_nacional_radio.instituto,
            Operador_nacional_radio.año_expediente, Operador_nacional_radio.número_expediente, Operador_nacional_radio.año_disposición, Operador_nacional_radio.número_disposición)
    
    def get_queryset(self):
        return Operador_nacional_radio.objects.all().order_by('-habilitación')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(context['object_list'], 100)
        page = self.request.GET.get('page')
        operadores_paginados = paginator.get_page(page)
        context['object_list'] = operadores_paginados
        return context

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(ver_OperadorNRadio), name='get')
class VerOperadordeRadio(DetailView):
    model = Operador_nacional_radio

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(actualizar_OperadorNRadio), name='get')
class ActualizarOPR(UpdateView):
    model = Operador_nacional_radio
    success_url = reverse_lazy('operadores_nacionales')
    form_class = RadioNacionalForm

############################################################# Operadores de TV ######################################################################

@login_required
@user_passes_test(ver_OperadorNTV)
def optvn_completos(request):
    optvnc = Operador_nacional_tv.objects.all()
    optvnc = pag_nacional(request, Operador_nacional_tv, completos_nacional)
    return render(request, 'Base_datos/operador_nacional_tv_completos.html', {'optvnc' : optvnc})

@login_required
@user_passes_test(ver_OperadorNTV)
def optvn_completos_exp(request):
    optvnc_exp = pag_nacional(request, Operador_nacional_tv, exp)
    return render(request, 'Base_datos/operador_nacional_tv_completos_exp.html', {'optvnc_exp' : optvnc_exp})

@login_required
@user_passes_test(ver_OperadorNTV)
def optvn_incompletos(request):
    optvn = pag_nacional(request, Operador_nacional_tv, incompletos_nacional)
    return render(request, 'Base_datos/optvn_incompletos.html', {'optvn' : optvn} )

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(carga_OperadorNTV), name='get')
class CrearOperadordeTV(CreateView):
    template_name = 'Base_datos/operador_nacional_tv_form.html'
    form_class = TVNacionalForm
    success_url = reverse_lazy('operadores_nacionales')

@method_decorator(login_required, name='get')
class ListarOperadordeTV(ListView):
    model = Operador_nacional_tv
    fields = (Operador_nacional_tv.apellido, Operador_nacional_tv.nombre, Operador_nacional_tv.DNI, Operador_nacional_tv.habilitación, Operador_nacional_tv.instituto,
            Operador_nacional_tv.año_expediente, Operador_nacional_tv.número_expediente, Operador_nacional_tv.año_disposición, Operador_nacional_tv.número_disposición)
    
    def get_queryset(self):
        return Operador_nacional_tv.objects.all().order_by('-habilitación')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(context['object_list'], 100)
        page = self.request.GET.get('page')
        operadores_paginados = paginator.get_page(page)
        context['object_list'] = operadores_paginados
        return context

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(ver_OperadorNTV), name='get')
class VerOperadordeTV(DetailView):
    model = Operador_nacional_tv

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(actualizar_OperadorNTV), name='get')
class ActualizarOPTV(UpdateView):
    model = Operador_nacional_tv
    success_url = reverse_lazy('operadores_nacionales')
    form_class = TVNacionalForm

############################################################# Operadores de Planta ######################################################################

@login_required
@user_passes_test(ver_OperadorNPlanta)
def opplantan_completos(request):
    opplantanc = pag_nacional(request, Operador_nacional_planta, completos_nacional)
    return render(request, 'Base_datos/operador_nacional_planta_completos.html', {'opplantanc' : opplantanc})

@login_required
@user_passes_test(ver_OperadorNPlanta)
def opplantan_completos_exp(request):
    opplantanc_exp = pag_nacional(request, Operador_nacional_planta, exp)
    return render(request, 'Base_datos/operador_nacional_planta_completos_exp.html', {'opplantanc_exp' : opplantanc_exp})

@login_required
@user_passes_test(ver_OperadorNPlanta)
def opplantan_incompletos(request):
    opplantan = pag_nacional(request, Operador_nacional_planta, incompletos_nacional)
    return render(request, 'Base_datos/opplantan_incompletos.html', {'opplantan' : opplantan} )

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(carga_OperadorNPlanta), name='get')
class CrearOperadordePlanta(CreateView):
    template_name = 'Base_datos/operador_nacional_planta_form.html'
    form_class = PlantaNacionalForm
    success_url = reverse_lazy('operadores_nacionales')

@method_decorator(login_required, name='get')
class ListarOperadordePlanta(ListView):
    model = Operador_nacional_planta
    fields = (Operador_nacional_planta.apellido, Operador_nacional_planta.nombre, Operador_nacional_planta.DNI, Operador_nacional_planta.habilitación, Operador_nacional_planta.instituto,
            Operador_nacional_planta.año_expediente, Operador_nacional_planta.número_expediente, Operador_nacional_planta.año_disposición, Operador_nacional_planta.número_disposición)
    
    def get_queryset(self):
        return Operador_nacional_planta.objects.all().order_by('-habilitación')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(context['object_list'], 100)
        page = self.request.GET.get('page')
        operadores_paginados = paginator.get_page(page)
        context['object_list'] = operadores_paginados
        return context

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(ver_OperadorNPlanta), name='get')
class VerOperadordePlanta(DetailView):
    model = Operador_nacional_planta

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(actualizar_OperadorNPlanta), name='get')
class ActualizarOPPlanta(UpdateView):
    model = Operador_nacional_planta
    success_url = reverse_lazy('operadores_nacionales')
    form_class = PlantaNacionalForm

############################################################# Operadores Locales ######################################################################

@login_required
def operadores_locales(request):
    return render(request, 'Base_datos/operadores_locales.html')

############################################################# Operadores de Radio ######################################################################

@login_required
@user_passes_test(ver_OperadorLRadio)
def oprl_completos(request):
    oprlc = pag_local(request, Operador_local_radio, completos_local)
    return render(request, 'Base_datos/operador_local_radio_completos.html', {'oprlc' : oprlc})

@login_required
@user_passes_test(ver_OperadorLRadio)
def oprl_completos_exp(request):
    oprlc_exp = pag_local(request, Operador_local_radio, exp)
    return render(request, 'Base_datos/operador_local_radio_completos_exp.html', {'oprlc_exp' : oprlc_exp})

@login_required
@user_passes_test(ver_OperadorLRadio)
def oprl_incompletos(request):
    oprl = pag_local(request, Operador_local_radio, incompletos_local)
    return render(request, 'Base_datos/oprl_incompletos.html', {'oprl' : oprl} )

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(carga_OperadorLRadio), name='get')
class CrearOperadordeRadioLocal(CreateView):
    template_name = 'Base_datos/operador_local_radio_form.html'
    form_class = RadioLocalForm
    success_url = reverse_lazy('operadores_locales')

@method_decorator(login_required, name='get')
class ListarOperadordeRadioLocal(ListView):
    model = Operador_local_radio
    fields = (Operador_local_radio.apellido, Operador_local_radio.nombre, Operador_local_radio.DNI, Operador_local_radio.habilitación,
            Operador_local_radio.año_expediente, Operador_local_radio.número_expediente, Operador_local_radio.año_disposición, Operador_local_radio.número_disposición)
    
    def get_queryset(self):
        return Operador_local_radio.objects.all().order_by('-habilitación')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(context['object_list'], 100)
        page = self.request.GET.get('page')
        operadores_paginados = paginator.get_page(page)
        context['object_list'] = operadores_paginados
        return context

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(ver_OperadorLRadio), name='get')
class VerOperadordeRadioLocal(DetailView):
    model = Operador_local_radio

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(ver_OperadorLRadio), name='get')
class ActualizarOPRLocal(UpdateView):
    model = Operador_local_radio
    success_url = reverse_lazy('operadores_locales')
    form_class = RadioLocalForm

############################################################# Operadores de TV ######################################################################

@login_required
@user_passes_test(ver_OperadorLTV)
def optvl_completos(request):
    optvlc = pag_local(request, Operador_local_tv, completos_local)
    return render(request, 'Base_datos/operador_local_tv_completos.html', {'optvlc' : optvlc})

@login_required
@user_passes_test(ver_OperadorLTV)
def optvl_completos_exp(request):
    optvlc_exp = pag_local(request, Operador_local_tv, exp)
    return render(request, 'Base_datos/operador_local_tv_completos_exp.html', {'optvlc_exp' : optvlc_exp})

@login_required
@user_passes_test(ver_OperadorLTV)
def optvl_incompletos(request):
    optvl = pag_local(request, Operador_local_tv, incompletos_local)
    return render(request, 'Base_datos/optvl_incompletos.html', {'optvl' : optvl} )

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(carga_OperadorLTV), name='get')
class CrearOperadordeTVLocal(CreateView):
    template_name = 'Base_datos/operador_local_tv_form.html'
    form_class = TVLocalForm
    success_url = reverse_lazy('operadores_locales')

@method_decorator(login_required, name='get')
class ListarOperadordeTVLocal(ListView):
    model = Operador_local_tv
    fields = (Operador_local_tv.apellido, Operador_local_tv.nombre, Operador_local_tv.DNI, Operador_local_tv.habilitación,
            Operador_local_tv.año_expediente, Operador_local_tv.número_expediente, Operador_local_tv.año_disposición, Operador_local_tv.número_disposición)
    
    def get_queryset(self):
        return Operador_local_tv.objects.all().order_by('-habilitación')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(context['object_list'], 100)
        page = self.request.GET.get('page')
        operadores_paginados = paginator.get_page(page)
        context['object_list'] = operadores_paginados
        return context

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(ver_OperadorLTV), name='get')
class VerOperadordeTVLocal(DetailView):
    model = Operador_local_tv

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(actualizar_OperadorLTV), name='get')
class ActualizarOPTVLocal(UpdateView):
    model = Operador_local_tv
    success_url = reverse_lazy('operadores_locales')
    form_class = TVLocalForm

############################################################# Operadores de Planta ######################################################################

@login_required
@user_passes_test(ver_OperadorLPlanta)
def opplantal_completos(request):
    opplantalc = pag_local(request, Operador_local_planta, completos_local)
    return render(request, 'Base_datos/operador_local_planta_completos.html', {'opplantalc' : opplantalc})

@login_required
@user_passes_test(ver_OperadorLPlanta)
def opplantal_completos_exp(request):
    opplantalc_exp = pag_local(request, Operador_local_planta, exp)
    return render(request, 'Base_datos/operador_local_planta_completos_exp.html', {'opplantalc_exp' : opplantalc_exp})

@login_required
@user_passes_test(ver_OperadorLPlanta)
def opplantal_incompletos(request):
    opplantal = pag_local(request, Operador_local_planta, incompletos_local)
    return render(request, 'Base_datos/opplantal_incompletos.html', {'opplantal' : opplantal} )

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(carga_OperadorLPlanta), name='get')
class CrearOperadordePlantaLocal(CreateView):
    template_name = 'Base_datos/operador_local_planta_form.html'
    form_class = PlantaLocalForm
    success_url = reverse_lazy('operadores_locales')

@method_decorator(login_required, name='get')
class ListarOperadordePlantaLocal(ListView):
    model = Operador_local_planta
    fields = (Operador_local_planta.apellido, Operador_local_planta.nombre, Operador_local_planta.DNI, Operador_local_planta.habilitación,
            Operador_local_planta.año_expediente, Operador_local_planta.número_expediente, Operador_local_planta.año_disposición, Operador_local_planta.número_disposición)
    
    def get_queryset(self):
        return Operador_local_planta.objects.all().order_by('-habilitación')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(context['object_list'], 100)
        page = self.request.GET.get('page')
        operadores_paginados = paginator.get_page(page)
        context['object_list'] = operadores_paginados
        return context

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(ver_OperadorLPlanta), name='get')
class VerOperadordePlantaLocal(DetailView):
    model = Operador_local_planta

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(actualizar_OperadorLPlanta), name='get')
class ActualizarOPPlantaLocal(UpdateView):
    model = Operador_local_planta
    success_url = reverse_lazy('operadores_locales')
    form_class = PlantaLocalForm

############################################################# Productores y Directores ######################################################################

@login_required
def productores(request):
    return render(request, 'Base_datos/productores_y_directores.html')

@login_required
@user_passes_test(ver_productor)
def prod_completos(request):
    prodc = pag_nacional(request, Productor, completos_nacional)
    return render(request, 'Base_datos/productores_completos.html', {'prodc' : prodc})

@login_required
@user_passes_test(ver_productor)
def prod_completos_exp(request):
    prodc_exp = pag_nacional(request, Productor, exp)
    return render(request, 'Base_datos/productores_completos_exp.html', {'prodc_exp' : prodc_exp})

@login_required
@user_passes_test(ver_productor)
def prod_incompletos(request):
    prod = pag_nacional(request, Productor, incompletos_nacional)
    return render(request, 'Base_datos/prod_incompletos.html', {'prod' : prod} )

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(carga_productor), name='get')
class CrearProductor(CreateView):
    template_name='Base_datos/productor_form.html'
    form_class= ProductorForm
    success_url = reverse_lazy('productores_y_directores')

@method_decorator(login_required, name='get')
class ListarProductor(ListView):
    model = Productor
    fields = (Productor.apellido, Productor.nombre, Productor.DNI, Productor.habilitación, Productor.instituto,
            Productor.año_expediente, Productor.número_expediente, Productor.año_disposición, Productor.número_disposición)
    
    def get_queryset(self):
        return Productor.objects.all().order_by('-habilitación')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(context['object_list'], 100)
        page = self.request.GET.get('page')
        productores_paginados = paginator.get_page(page)
        context['object_list'] = productores_paginados
        return context

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(ver_productor), name='get')
class VerProductor(DetailView):
    model = Productor

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(actualizar_productor), name='get')
class ActualizarProd(UpdateView):
    model = Productor
    success_url = reverse_lazy('productores_y_directores')
    form_class = ProductorForm

############################################################# Guionistas ######################################################################

@login_required
def guionistas(request):
    return render(request, 'Base_datos/guionistas.html')

@login_required
@user_passes_test(ver_guionista)
def guion_completos(request):
    guionc = pag_nacional(request, Guionista, completos_nacional)
    return render(request, 'Base_datos/guionistas_completos.html', {'guionc' : guionc})

@login_required
@user_passes_test(ver_guionista)
def guion_completos_exp(request):
    guionc_exp = pag_nacional(request, Guionista, exp)
    return render(request, 'Base_datos/guionistas_completos_exp.html', {'guionc_exp' : guionc_exp})

@login_required
@user_passes_test(ver_guionista)
def guion_incompletos(request):
    guion = pag_nacional(request, Guionista, incompletos_nacional)
    return render(request, 'Base_datos/guion_incompletos.html', {'guion' : guion} )

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(carga_guionista), name='get')
class CrearGuionista(CreateView):
    template_name = 'Base_datos/guionista_form.html'
    form_class = GuionistaForm
    success_url = reverse_lazy('guionistas')

@method_decorator(login_required, name='get')
class ListarGuionista(ListView):
    model = Guionista
    fields = (Guionista.apellido, Guionista.nombre, Guionista.DNI, Guionista.habilitación, Guionista.instituto,
            Guionista.año_expediente, Guionista.número_expediente, Guionista.año_disposición, Guionista.número_disposición)
    
    def get_queryset(self):
        return Guionista.objects.all().order_by('-habilitación')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(context['object_list'], 100)
        page = self.request.GET.get('page')
        guionistas_paginados = paginator.get_page(page)
        context['object_list'] = guionistas_paginados
        return context

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(ver_guionista), name='get')
class VerGuionista(DetailView):
    model = Guionista

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(actualizar_guionista), name='get')
class ActualizarGuion(UpdateView):
    model = Guionista
    success_url = reverse_lazy('guionistas')
    form_class = GuionistaForm
"""servidor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.admin.views.decorators import staff_member_required
from Base_datos.views import (index, buscar,
                              locutores, ln_incompletos,CrearLocutorNacional, ListarLocutorNacional, VerLocutorNacional, ActualizarLN,
                              locutor_local, ll_incompletos, CrearLocutorLocal, ListarLocutorLocal, VerLocutorLocal, ActualizarLL,
                              operadores_nacionales,
                              oprn_incompletos, CrearOperadordeRadio, ListarOperadordeRadio, VerOperadordeRadio, ActualizarOPR,
                              optvn_incompletos ,CrearOperadordeTV, ListarOperadordeTV, VerOperadordeTV, ActualizarOPTV,
                              opplantan_incompletos ,CrearOperadordePlanta, ListarOperadordePlanta, VerOperadordePlanta, ActualizarOPPlanta,
                              operadores_locales,
                              oprl_incompletos, CrearOperadordeRadioLocal, ListarOperadordeRadioLocal, VerOperadordeRadioLocal, ActualizarOPRLocal,
                              optvl_incompletos, CrearOperadordeTVLocal, ListarOperadordeTVLocal, VerOperadordeTVLocal, ActualizarOPTVLocal,
                              opplantal_incompletos, CrearOperadordePlantaLocal, ListarOperadordePlantaLocal, VerOperadordePlantaLocal, ActualizarOPPlantaLocal,)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('buscar/', buscar, name='buscar'),

    path('locutores_nacionales/', locutores, name='locutores_nacionales'),
    path('carga_locutor_nacional/', CrearLocutorNacional.as_view(), name='carga_locutor_nacional'),
    path('lista_locutores_nacionales/', ListarLocutorNacional.as_view(), name='lista_locutor_nacional'),
    path('locutores_nacionales_incompletos/', ln_incompletos, name= 'ln_incompletos'),
    path('locutor_nacional/<int:pk>/', VerLocutorNacional.as_view(), name='ver_locutor'),
    path('locutor_nacional/<int:pk>/actualizar', ActualizarLN.as_view(), name='actualizar_ln'),

    path('locutores_locales/', locutor_local, name='locutores_locales'),
    path('carga_locutor_local/', CrearLocutorLocal.as_view(), name='carga_locutor_local'),
    path('lista_locutores_locales/', ListarLocutorLocal.as_view(), name='lista_locutor_local'),
    path('locutores_locales_incompletos/', ll_incompletos, name='ll_incompletos'),
    path('locutor_local/<int:pk>/', VerLocutorLocal.as_view(), name='ver_locutor_local'),
    path('locutor_local/<int:pk>/actualizar', ActualizarLL.as_view(), name='actualizar_ll'),

    path('operadores_nacionales/', operadores_nacionales, name='operadores_nacionales'),

    path('carga_operador_nacional_radio', CrearOperadordeRadio.as_view(), name='carga_operador_radio'),
    path('lista_operador_nacional_radio', ListarOperadordeRadio.as_view(), name='lista_operador_nacional_radio'),
    path('operadores_nacionales_radio', oprn_incompletos, name='oprn_incompletos'),
    path('operador_nacional_radio/<int:pk>/', VerOperadordeRadio.as_view(), name='ver_operador_nacional_radio'),
    path('operador_nacional_radio/<int:pk>/actualizar', ActualizarOPR.as_view(), name='actualizar_operador_nacional_radio'),

    path('carga_operador_nacional_tv', CrearOperadordeTV.as_view(), name='carga_operador_tv'),
    path('lista_operador_nacional_tv', ListarOperadordeTV.as_view(), name='lista_operador_nacional_tv'),
    path('operadores_nacionales_tv', optvn_incompletos, name='optvn_incompletos'),
    path('operador_nacional_tv/<int:pk>/', VerOperadordeTV.as_view(), name='ver_operador_nacional_tv'),
    path('operador_nacional_tv/<int:pk>/actualizar', ActualizarOPTV.as_view(), name='actualizar_operador_nacional_tv'),

    path('carga_operador_nacional_planta', CrearOperadordePlanta.as_view(), name='carga_operador_planta'),
    path('lista_operador_nacional_planta', ListarOperadordePlanta.as_view(), name='lista_operador_nacional_planta'),
    path('operadores_nacionales_planta', opplantan_incompletos, name='opplantan_incompletos'),
    path('operador_nacional_planta/<int:pk>/', VerOperadordePlanta.as_view(), name='ver_operador_nacional_planta'),
    path('operador_nacional_planta/<int:pk>/actualizar', ActualizarOPPlanta.as_view(), name='actualizar_operador_nacional_planta'),

    path('operadores_locales/', operadores_locales, name='operadores_locales'),

    path('carga_operador_local_radio', CrearOperadordeRadioLocal.as_view(), name='carga_operador_radio_local'),
    path('lista_operador_local_radio', ListarOperadordeRadioLocal.as_view(), name='lista_operador_local_radio'),
    path('operadores_local_radio', oprl_incompletos, name='oprl_incompletos'),
    path('operador_local_radio/<int:pk>/', VerOperadordeRadioLocal.as_view(), name='ver_operador_local_radio'),
    path('operador_local_radio/<int:pk>/actualizar', ActualizarOPRLocal.as_view(), name='actualizar_operador_local_radio'),

    path('carga_operador_local_tv', CrearOperadordeTVLocal.as_view(), name='carga_operador_tv_local'),
    path('lista_operador_local_tv', ListarOperadordeTVLocal.as_view(), name='lista_operador_local_tv'),
    path('operadores_local_tv', optvl_incompletos, name='optvl_incompletos'),
    path('operador_local_tv/<int:pk>/', VerOperadordeTVLocal.as_view(), name='ver_operador_local_tv'),
    path('operador_local_tv/<int:pk>/actualizar', ActualizarOPTVLocal.as_view(), name='actualizar_operador_local_tv'),

    path('carga_operador_local_planta', CrearOperadordePlantaLocal.as_view(), name='carga_operador_planta_local'),
    path('lista_operador_local_planta', ListarOperadordePlantaLocal.as_view(), name='lista_operador_local_planta'),
    path('operadores_local_planta', opplantal_incompletos, name='opplantal_incompletos'),
    path('operador_local_planta/<int:pk>/', VerOperadordePlantaLocal.as_view(), name='ver_operador_local_planta'),
    path('operador_local_planta/<int:pk>/actualizar', ActualizarOPPlantaLocal.as_view(), name='actualizar_operador_local_planta'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
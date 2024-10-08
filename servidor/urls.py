from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.admin.views.decorators import staff_member_required
from Base_datos.views import (index, buscar, UserSingUp, UserLogin, UserLogout, ChangePassword,
                            locutores, ln_completos, ln_completos_exp,ln_incompletos, CrearLocutorNacional, ListarLocutorNacional, VerLocutorNacional, ActualizarLN, BorrarLN,
                            locutor_local, ll_completos, ll_completos_exp,ll_incompletos, ll_archivo, CrearLocutorLocal, ListarLocutorLocal, VerLocutorLocal, ActualizarLL, BorrarLL,
                            operadores_nacionales,
                            oprn_completos, oprn_completos_exp, oprn_incompletos, CrearOperadordeRadio, ListarOperadordeRadio, VerOperadordeRadio, ActualizarOPR, BorrarOPR,
                            optvn_completos, optvn_completos_exp,optvn_incompletos, CrearOperadordeTV, ListarOperadordeTV, VerOperadordeTV, ActualizarOPTV, BorrarOPTV,
                            opplantan_completos, opplantan_completos_exp,opplantan_incompletos, CrearOperadordePlanta, ListarOperadordePlanta, VerOperadordePlanta, ActualizarOPPlanta, BorrarOPPlanta,
                            operadores_locales,
                            oprl_completos, oprl_completos_exp,oprl_incompletos, oprl_archivo, CrearOperadordeRadioLocal, ListarOperadordeRadioLocal, VerOperadordeRadioLocal, ActualizarOPRLocal, BorrarOPRLocal,
                            optvl_completos, optvl_completos_exp,optvl_incompletos, optvl_archivo, CrearOperadordeTVLocal, ListarOperadordeTVLocal, VerOperadordeTVLocal, ActualizarOPTVLocal, BorrarOPTVLocal,
                            opplantal_completos, opplantal_completos_exp, opplantal_archivo, opplantal_incompletos, CrearOperadordePlantaLocal, ListarOperadordePlantaLocal, VerOperadordePlantaLocal, ActualizarOPPlantaLocal, BorrarOPPlantaLocal,
                            productores, prod_completos, prod_completos_exp, prod_incompletos, CrearProductor, ListarProductor, VerProductor, ActualizarProd, BorrarProd,
                            guionistas, guion_completos, guion_completos_exp,guion_incompletos, CrearGuionista, ListarGuionista, VerGuionista, ActualizarGuion, BorrarGuion)
from expedientes.views import (expedientes, carnets, expedientes_finalizados, calculadora_anual, buscar_expedientes, año, CrearExpediente, ListarExpedientes, ActualizarExpediente, BorrarExpediente)
from correo.views import correo, correo_finalizados, buscar_envio, NuevoEnvio, ListarCorreo, ActualizarCorreo, CorreoBorrar
from Libros.views import libros, buscar_acta, NuevoLibro, ListarLibros, ActualizarLibro, NuevaActa, ListarActas, DetalleActa, ActualizarActa, Profesor

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('buscar/', buscar, name='buscar'),
    path('alta_usuario/', staff_member_required(UserSingUp.as_view()), name='alta_usuario'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(next_page='/'), name='logout'),
    path('change_password/', ChangePassword.as_view(), name='change_password'),

    #Locutores Nacionales

    path('locutores_nacionales/', locutores, name='locutores_nacionales'),
    path('carga_locutor_nacional/', CrearLocutorNacional.as_view(), name='carga_locutor_nacional'),
    path('lista_locutores_nacionales/', ListarLocutorNacional.as_view(), name='lista_locutor_nacional'),
    path('locutores_nacionales_completos/', ln_completos, name= 'ln_completos'),
    path('locutores_nacionales_completos_expedientes/', ln_completos_exp, name= 'ln_completos_exp'),
    path('locutores_nacionales_incompletos/', ln_incompletos, name= 'ln_incompletos'),
    path('locutor_nacional/<int:pk>/', VerLocutorNacional.as_view(), name='ver_locutor'),
    path('locutor_nacional/<int:pk>/actualizar/', ActualizarLN.as_view(), name='actualizar_ln'),
    path('locutor_nacional/<int:pk>/borrar/', BorrarLN.as_view(), name='borrar_ln'),

    #Locutores Locales

    path('locutores_locales/', locutor_local, name='locutores_locales'),
    path('carga_locutor_local/', CrearLocutorLocal.as_view(), name='carga_locutor_local'),
    path('lista_locutores_locales/', ListarLocutorLocal.as_view(), name='lista_locutor_local'),
    path('locutores_locales_completos/', ll_completos, name='ll_completos'),
    path('locutores_locales_completos_expedientes/', ll_completos_exp, name='ll_completos_exp'),
    path('locutores_locales_incompletos/', ll_incompletos, name='ll_incompletos'),
    path('locutores_locales_archivo/', ll_archivo, name='ll_archivo'),
    path('locutor_local/<int:pk>/', VerLocutorLocal.as_view(), name='ver_locutor_local'),
    path('locutor_local/<int:pk>/actualizar/', ActualizarLL.as_view(), name='actualizar_ll'),
    path('locutor_local/<int:pk>/borrar/', BorrarLL.as_view(), name='borrar_ll'),

    ##########################Operadores Nacionales######################################################

    path('operadores_nacionales/', operadores_nacionales, name='operadores_nacionales'),

    #Operadores de Radio

    path('carga_operador_nacional_radio/', CrearOperadordeRadio.as_view(), name='carga_operador_radio'),
    path('lista_operador_nacional_radio/', ListarOperadordeRadio.as_view(), name='lista_operador_nacional_radio'),
    path('operadores_nacionales_radio_completos/', oprn_completos, name='oprn_completos'),
    path('operadores_nacionales_radio_completos_expedientes/', oprn_completos_exp, name='oprn_completos_exp'),
    path('operadores_nacionales_radio_incompletos/', oprn_incompletos, name='oprn_incompletos'),
    path('operador_nacional_radio/<int:pk>/', VerOperadordeRadio.as_view(), name='ver_operador_nacional_radio'),
    path('operador_nacional_radio/<int:pk>/actualizar/', ActualizarOPR.as_view(), name='actualizar_operador_nacional_radio'),
    path('operador_nacional_radio/<int:pk>/borrar/', BorrarOPR.as_view(), name='borrar_operador_nacional_radio'),

    #Operadores de TV

    path('carga_operador_nacional_tv/', CrearOperadordeTV.as_view(), name='carga_operador_tv'),
    path('lista_operador_nacional_tv/', ListarOperadordeTV.as_view(), name='lista_operador_nacional_tv'),
    path('operadores_nacionales_tv_completos/', optvn_completos, name='optvn_completos'),
    path('operadores_nacionales_tv_completos_expedientes/', optvn_completos_exp, name='optvn_completos_exp'),
    path('operadores_nacionales_tv_incompletos/', optvn_incompletos, name='optvn_incompletos'),
    path('operador_nacional_tv/<int:pk>/', VerOperadordeTV.as_view(), name='ver_operador_nacional_tv'),
    path('operador_nacional_tv/<int:pk>/actualizar/', ActualizarOPTV.as_view(), name='actualizar_operador_nacional_tv'),
    path('operador_nacional_tv/<int:pk>/borrar/', BorrarOPTV.as_view(), name='borrar_operador_nacional_tv'),

    #Operadores de Planta Transmisora

    path('carga_operador_nacional_planta/', CrearOperadordePlanta.as_view(), name='carga_operador_planta'),
    path('lista_operador_nacional_planta/', ListarOperadordePlanta.as_view(), name='lista_operador_nacional_planta'),
    path('operadores_nacionales_planta_completos/', opplantan_completos, name='opplantan_completos'),
    path('operadores_nacionales_planta_completos_expedientes/', opplantan_completos_exp, name='opplantan_completos_exp'),
    path('operadores_nacionales_planta_incompletos/', opplantan_incompletos, name='opplantan_incompletos'),
    path('operador_nacional_planta/<int:pk>/', VerOperadordePlanta.as_view(), name='ver_operador_nacional_planta'),
    path('operador_nacional_planta/<int:pk>/actualizar/', ActualizarOPPlanta.as_view(), name='actualizar_operador_nacional_planta'),
    path('operador_nacional_planta/<int:pk>/borrar/', BorrarOPPlanta.as_view(), name='borrar_operador_nacional_planta'),

    ###########################Operadores Locales####################################

    path('operadores_locales/', operadores_locales, name='operadores_locales'),

    #Operadores de Radio

    path('carga_operador_local_radio/', CrearOperadordeRadioLocal.as_view(), name='carga_operador_radio_local'),
    path('lista_operador_local_radio/', ListarOperadordeRadioLocal.as_view(), name='lista_operador_local_radio'),
    path('operadores_local_radio_completos/', oprl_completos, name='oprl_completos'),
    path('operadores_local_radio_completos_expedientes/', oprl_completos_exp, name='oprl_completos_exp'),
    path('operadores_local_radio_incompletos/', oprl_incompletos, name='oprl_incompletos'),
    path('operadores_local_radio_archivo/', oprl_archivo, name='oprl_archivo'),
    path('operador_local_radio/<int:pk>/', VerOperadordeRadioLocal.as_view(), name='ver_operador_local_radio'),
    path('operador_local_radio/<int:pk>/actualizar/', ActualizarOPRLocal.as_view(), name='actualizar_operador_local_radio'),
    path('operador_local_radio/<int:pk>/borrar/', BorrarOPRLocal.as_view(), name='borrar_operador_local_radio'),

    #Operadores de TV

    path('carga_operador_local_tv/', CrearOperadordeTVLocal.as_view(), name='carga_operador_tv_local'),
    path('lista_operador_local_tv/', ListarOperadordeTVLocal.as_view(), name='lista_operador_local_tv'),
    path('operadores_local_tv_completos/', optvl_completos, name='optvl_completos'),
    path('operadores_local_tv_completos_expedientes/', optvl_completos_exp, name='optvl_completos_exp'),
    path('operadores_local_tv_incompletos/', optvl_incompletos, name='optvl_incompletos'),
    path('operadores_local_tv_archivo/', optvl_archivo, name='optvl_archivo'),
    path('operador_local_tv/<int:pk>/', VerOperadordeTVLocal.as_view(), name='ver_operador_local_tv'),
    path('operador_local_tv/<int:pk>/actualizar/', ActualizarOPTVLocal.as_view(), name='actualizar_operador_local_tv'),
    path('operador_local_tv/<int:pk>/borrar/', BorrarOPTVLocal.as_view(), name='borrar_operador_local_tv'),

    #Operadores de Planta Transmisora

    path('carga_operador_local_planta/', CrearOperadordePlantaLocal.as_view(), name='carga_operador_planta_local'),
    path('lista_operador_local_planta/', ListarOperadordePlantaLocal.as_view(), name='lista_operador_local_planta'),
    path('operadores_local_planta_completos/', opplantal_completos, name='opplantal_completos'),
    path('operadores_local_planta_completos_expedientes/', opplantal_completos_exp, name='opplantal_completos_exp'),
    path('operadores_local_planta_incompletos/', opplantal_incompletos, name='opplantal_incompletos'),
    path('operadores_local_planta_archivo/', opplantal_archivo, name='opplantal_archivo'),
    path('operador_local_planta/<int:pk>/', VerOperadordePlantaLocal.as_view(), name='ver_operador_local_planta'),
    path('operador_local_planta/<int:pk>/actualizar/', ActualizarOPPlantaLocal.as_view(), name='actualizar_operador_local_planta'),
    path('operador_local_planta/<int:pk>/borrar/', BorrarOPPlantaLocal.as_view(), name='borrar_operador_local_planta'),

    ###################################Productores y Directores##############################################

    path('productores_y_directores/', productores, name='productores_y_directores'),
    path('carga_productor_y_director/', CrearProductor.as_view(), name='carga_productor'),
    path('lista_productores_y_directores/', ListarProductor.as_view(), name='lista_productor_y_director'),
    path('productores_completos/', prod_completos, name= 'prod_completos'),
    path('productores_completos_expedientes/', prod_completos_exp, name= 'prod_completos_exp'),
    path('productores_incompletos/', prod_incompletos, name= 'prod_incompletos'),
    path('productor_y_director/<int:pk>/', VerProductor.as_view(), name='ver_productor'),
    path('productor_y_director/<int:pk>/actualizar/', ActualizarProd.as_view(), name='actualizar_prod'),
    path('productor_y_director/<int:pk>/borrar/', BorrarProd.as_view(), name='borrar_prod'),

    #Guionistas

    path('guionistas/', guionistas, name='guionistas'),
    path('carga_guionista/', CrearGuionista.as_view(), name='carga_guionista'),
    path('lista_guionistas/', ListarGuionista.as_view(), name='lista_guionista'),
    path('guionistas_completos/', guion_completos, name= 'guion_completos'),
    path('guionistas_completos_expedientes/', guion_completos_exp, name= 'guion_completos_exp'),
    path('guionistas_incompletos/', guion_incompletos, name= 'guion_incompletos'),
    path('guionista/<int:pk>/', VerGuionista.as_view(), name='ver_guionista'),
    path('guionista/<int:pk>/actualizar/', ActualizarGuion.as_view(), name='actualizar_guion'),
    path('guionista/<int:pk>/borrar/', BorrarGuion.as_view(), name='borrar_guion'),

    #############Expedientes###############

    path('expedientes/', expedientes, name='expedientes'),
    path('expedientes/cargar/', CrearExpediente.as_view(), name='carga_expediente'),
    path('lista_expedientes/', ListarExpedientes.as_view(), name='lista_expedientes'),
    path('carnets/', carnets, name='carnets'),
    path('expedientes_finalizados/', expedientes_finalizados, name='expedientes_finalizados'),
    path('expediente/<int:pk>/actualizar', ActualizarExpediente.as_view(), name='actualizar_expediente'),
    path('expedientes/ingresar_año/', año, name='meta'),
    path('expediente/calcular/<int:anio_actual>', calculadora_anual, name='calculadora'),
    path('buscar/expedientes/', buscar_expedientes, name='buscar_expedientes'),
    path('expediente/<int:pk>/borrar', staff_member_required(BorrarExpediente.as_view()), name='borrar_expediente'),

    ###############Correo#########################
    
    path('correo/', correo, name='correo'),
    path('correo/nuevo_envio/', NuevoEnvio.as_view(), name='nuevo_envio'),
    path('correo/listar/', ListarCorreo.as_view(), name='listar_correo'),
    path('correo/<int:pk>/actualizar/', ActualizarCorreo.as_view(), name='actualizar_correo'),
    path('correo/finalizados/', correo_finalizados, name='correo_finalizados' ),
    path('buscar/envio/', buscar_envio, name='buscar_envio'),
    path('correo/borrar/<int:pk>/', staff_member_required(CorreoBorrar.as_view()), name='borrar_correo'),

    ############Libros de Actas######################

    path('libros/', libros, name='libros'),
    path('libros/nuevo_libro/', NuevoLibro.as_view(), name='nuevo_libro'),
    path('libros/listar_libros/', ListarLibros.as_view(), name='listar_libros'),
    path('libros/actualizar/<int:pk>/', ActualizarLibro.as_view(), name='actualizar_libro'),
    path('libros/actas/nueva_acta/', NuevaActa.as_view(), name='nueva_acta'),
    path('libros/actas/listar_actas/<str:nombre>', ListarActas.as_view(), name='listar_actas'),
    path('libros/actas/detalle/<int:pk>/', DetalleActa.as_view(), name='detalle_acta'),
    path('libros/actas/actualizar/<int:pk>/', ActualizarActa.as_view(), name='actualizar_acta'),
    path('libros/actas/nueva_firma/', Profesor.as_view(), name='nueva_firma'),
    path('libros/actas/buscar', buscar_acta, name='buscar_acta'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.shortcuts import render
from expedientes.forms import ExpedienteForm
from expedientes.models import Expediente
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.db.models import Sum
from django.utils import timezone

@login_required
def expedientes(request):
    return render(request, 'expedientes/expedientes.html')

orden_categorias = [
        'Locutores Nacionales',
        'Locutores Locales',
        'Operadores Nacionales Varios',
        'Operadores Nacionales de Radio',
        'Operadores Nacionales de TV',
        'Operadores Nacionales de Planta Transmisora',
        'Operadores Locales Varios',
        'Operadores Locales de Radio',
        'Operadores Locales de TV',
        'Operadores Locales de Planta Transmisora',
        'Productores y Directores para Radio y TV',
        'Guionistas de Radio y TV',
    ]

meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

trimestres = [meses[0:3], meses[3:6], meses[6:9], meses[9:12]]

def obtener_categorias_y_totales(mes, anio_actual=True):
    if anio_actual:
        expedientes = Expediente.objects.filter(Fecha_de_disposición__year=timezone.now().year, Fecha_de_disposición__month=mes)
    else:
        anio_anterior = timezone.now().year - 1
        expedientes = Expediente.objects.filter(Fecha_de_disposición__year=anio_anterior, Fecha_de_disposición__month=mes)

    categorias_con_total = expedientes.values('Categoría').annotate(total_habilitados=Sum('Cantidad_de_Habilitados'))
    categorias_dict = {categoria['Categoría']: categoria['total_habilitados'] for categoria in categorias_con_total}
    total_todas_categorias = sum(categorias_dict.values())
    categorias_ordenadas = sorted(categorias_dict.items(), key=lambda x: orden_categorias.index(x[0]))
    return categorias_ordenadas, total_todas_categorias

def calcular_trimestres(anio_actual=True):
    datos_trimestrales = []

    for trimestre_actual in trimestres:
        trimestre_data = []
        categorias_dict_trimestral = {}

        for mes in trimestre_actual:
            mes_index = meses.index(mes) + 1
            categorias_ordenadas, total_todas_categorias = obtener_categorias_y_totales(mes_index, anio_actual)
            
            for categoria, total_categoria in categorias_ordenadas:
                if categoria in categorias_dict_trimestral:
                    categorias_dict_trimestral[categoria] += total_categoria
                else:
                    categorias_dict_trimestral[categoria] = total_categoria

        categorias_ordenadas_trimestral = sorted(categorias_dict_trimestral.items(), key=lambda x: orden_categorias.index(x[0]))
        total_todas_categorias_trimestral = sum(categorias_dict_trimestral.values())

        trimestre_data.append((categorias_ordenadas_trimestral, total_todas_categorias_trimestral))

        datos_trimestrales.append(trimestre_data)

    return datos_trimestrales

@login_required
def calculadora_anual(request):
    datos_anuales = []
    
    for i in range(len(meses)):
        mes = meses[i]
        categorias_ordenadas, total_todas_categorias = obtener_categorias_y_totales(i+1)
        datos_anuales.append((mes, categorias_ordenadas, total_todas_categorias))
    
    categorias_con_total_anual = Expediente.objects.filter(Fecha_de_disposición__year=timezone.now().year).values('Categoría').annotate(total_habilitados=Sum('Cantidad_de_Habilitados'))
    categorias_dict_anual = {categoria['Categoría']: categoria['total_habilitados'] for categoria in categorias_con_total_anual}
    total_todas_categorias_anual = sum(categorias_dict_anual.values())
    categorias_ordenadas_anual = sorted(categorias_dict_anual.items(), key=lambda x: orden_categorias.index(x[0]))

    datos_trimestrales = calcular_trimestres()

    context = {
        'orden_categorias': orden_categorias,
        'datos_anuales': datos_anuales,
        'categorias_ordenadas_anual': categorias_ordenadas_anual,
        'total_todas_categorias_anual': total_todas_categorias_anual,
        'datos_trimestrales' : datos_trimestrales,
    }

    return render(request, 'expedientes/calculadora.html', context)

@login_required
def calculadora_anual_anio_anterior(request):
    datos_anuales = []
    anio_actual = timezone.now().year
    anio_anterior = anio_actual - 1
    
    for i in range(len(meses)):
        mes = meses[i]
        categorias_ordenadas, total_todas_categorias = obtener_categorias_y_totales(i+1, False)
        datos_anuales.append((mes, categorias_ordenadas, total_todas_categorias))
    
    categorias_con_total_anual = Expediente.objects.filter(Fecha_de_disposición__year=anio_anterior).values('Categoría').annotate(total_habilitados=Sum('Cantidad_de_Habilitados'))
    categorias_dict_anual = {categoria['Categoría']: categoria['total_habilitados'] for categoria in categorias_con_total_anual}
    total_todas_categorias_anual = sum(categorias_dict_anual.values())
    categorias_ordenadas_anual = sorted(categorias_dict_anual.items(), key=lambda x: orden_categorias.index(x[0]))

    datos_trimestrales = calcular_trimestres(False)

    context = {
        'orden_categorias_anio_anterior': orden_categorias,
        'datos_anuales_anio_anterior': datos_anuales,
        'categorias_ordenadas_anual_anio_anterior': categorias_ordenadas_anual,
        'total_todas_categorias_anual_anio_anterior': total_todas_categorias_anual,
        'datos_trimestrales_anio_anterior': datos_trimestrales,
        'anio_anterior' : anio_anterior,
    }

    return render(request, 'expedientes/año_pasado.html', context)


@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(lambda u: u.groups.filter(name='Registro').exists()), name='get')
class CrearExpediente(CreateView):
    template_name = 'expedientes/expediente_form.html'
    form_class = ExpedienteForm
    success_url = reverse_lazy('expedientes')

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(lambda u: u.groups.filter(name='Registro').exists()), name='get')
class ListarExpedientes(ListView):
    model = Expediente
    fields = Expediente.Año_de_Expediente, Expediente.Número_de_Expediente, Expediente.Categoría, Expediente.Instituto_o_Localidad, Expediente.Fecha_de_Creación, Expediente.Estado

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(lambda u: u.groups.filter(name='Registro').exists()), name='get')
class ActualizarExpediente(UpdateView):
    model = Expediente
    success_url = reverse_lazy('expedientes')
    fields = '__all__'
from django.shortcuts import render, redirect
from expedientes.forms import ExpedienteForm
from expedientes.models import Expediente
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.db.models import Sum
from django.db.models import Q

def permiso_carga(user):
    return user.has_perm('expedientes.add_expediente')

def permiso_actualizar(user):
    return user.has_perm('expedientes.change_expediente')

def permiso_borrar(user):
    return user.has_perm('expedientes.delete_expediente')

def permiso_ver(user):
    return user.has_perm('expedientes.view_expediente')

@login_required
def expedientes(request):
    return render(request, 'expedientes/expedientes.html')

@login_required
@user_passes_test(permiso_ver)
def expedientes_finalizados(request):
    expe = Expediente.objects.all().order_by('-Fecha_de_Creación')
    return render(request, 'expedientes/expedientes_finalizados.html', {'expe' : expe})

@login_required
@user_passes_test(permiso_ver)
def buscar_expedientes(request):
    query = request.GET.get('q')
    resultados_expedientes = Expediente.objects.filter(Q(Año_de_Expediente__icontains=query) | Q(Número_de_Expediente__icontains=query))
    return render(request, 'expedientes/resultados_expedientes.html', {'resultados_expedientes': resultados_expedientes})

@login_required
@user_passes_test(permiso_ver)
def año(request):
    if request.method == 'POST':
        anio_actual = request.POST.get('anio_actual', '')
        if anio_actual:
            return redirect('calculadora', anio_actual)
    return render(request, 'expedientes/ingresar_año.html')

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

def obtener_categorias_y_totales(mes, anio_actual):
    if anio_actual:
        expedientes = Expediente.objects.filter(Fecha_de_disposición__year=anio_actual, Fecha_de_disposición__month=mes)

    categorias_con_total = expedientes.values('Categoría').annotate(total_habilitados=Sum('Cantidad_de_Habilitados'))
    categorias_dict = {categoria['Categoría']: categoria['total_habilitados'] for categoria in categorias_con_total}
    total_todas_categorias = sum(categorias_dict.values())
    categorias_ordenadas = sorted(categorias_dict.items(), key=lambda x: orden_categorias.index(x[0]))
    return categorias_ordenadas, total_todas_categorias

def calcular_trimestres(anio_actual):
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
def calculadora_anual(request, anio_actual):
    datos_anuales = []
    
    for i in range(len(meses)):
        mes = meses[i]
        categorias_ordenadas, total_todas_categorias = obtener_categorias_y_totales(i+1, anio_actual)
        datos_anuales.append((mes, categorias_ordenadas, total_todas_categorias))
    
    categorias_con_total_anual = Expediente.objects.filter(Fecha_de_disposición__year=anio_actual).values('Categoría').annotate(total_habilitados=Sum('Cantidad_de_Habilitados'))
    categorias_dict_anual = {categoria['Categoría']: categoria['total_habilitados'] for categoria in categorias_con_total_anual}
    total_todas_categorias_anual = sum(categorias_dict_anual.values())
    categorias_ordenadas_anual = sorted(categorias_dict_anual.items(), key=lambda x: orden_categorias.index(x[0]))

    datos_trimestrales = calcular_trimestres(anio_actual)

    context = {
        'año' : anio_actual,
        'orden_categorias': orden_categorias,
        'datos_anuales': datos_anuales,
        'categorias_ordenadas_anual': categorias_ordenadas_anual,
        'total_todas_categorias_anual': total_todas_categorias_anual,
        'datos_trimestrales' : datos_trimestrales,
    }

    return render(request, 'expedientes/calculadora.html', context)

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(permiso_carga), name='get')
class CrearExpediente(CreateView):
    template_name = 'expedientes/expediente_form.html'
    form_class = ExpedienteForm
    success_url = reverse_lazy('expedientes')

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(permiso_ver), name='get')
class ListarExpedientes(ListView):
    model = Expediente
    fields = Expediente.Año_de_Expediente, Expediente.Número_de_Expediente, Expediente.Categoría, Expediente.Instituto_o_Localidad, Expediente.Fecha_de_Creación, Expediente.Estado

    def get_queryset(self):
        return Expediente.objects.all().order_by('-Fecha_de_Creación')

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(permiso_actualizar), name='get')
class ActualizarExpediente(UpdateView):
    model = Expediente
    success_url = reverse_lazy('expedientes')
    fields = '__all__'

@method_decorator(login_required, name='get')
@method_decorator(user_passes_test(permiso_borrar), name='get')
class BorrarExpediente(DeleteView):
    model = Expediente
    success_url = reverse_lazy('expedientes')
    field = 'all'
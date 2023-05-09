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
from Base_datos.views import (index, locutores, ln_incompletos,CrearLocutorNacional, ListarLocutorNacional, VerLocutorNacional, ActualizarLN,
                              locutor_local, ll_incompletos, CrearLocutorLocal, ListarLocutorLocal, VerLocutorLocal, ActualizarLL)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
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
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
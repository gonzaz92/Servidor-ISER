from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Base_datos.models import (Locutor_nacional, Operador_nacional_radio, Operador_nacional_tv, Operador_nacional_planta,
                                Locutor_local, Operador_local_radio, Operador_local_tv, Operador_local_planta,
                                Productor, Guionista)

class UsuarioForm(UserCreationForm):
    username = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

######################### Locutor Nacional #######################################

class LocutorNacionalForm(forms.ModelForm):
    class Meta:
        model = Locutor_nacional
        fields = '__all__'
        widgets = {
            'apellido': forms.TextInput(),
            'nombre': forms.TextInput(),
            'DNI': forms.NumberInput(),
            'año_formulario': forms.NumberInput(attrs={'size': 5}),
            'formulario': forms.NumberInput(attrs={'size': 10}),
            'año_dni': forms.NumberInput(attrs={'size': 5}),
            'pdf_dni': forms.NumberInput(attrs={'size': 10}),
            'secundario': forms.NumberInput(attrs={'size': 5}),
            'pdf_secundario': forms.NumberInput(attrs={'size': 10}),
            'instituto': forms.TextInput(),
            'año_instituto': forms.NumberInput(attrs={'size': 5}),
            'pdf_instituto': forms.NumberInput(attrs={'size': 10}),
            'año_acta': forms.NumberInput(attrs={'size': 5}),
            'acta': forms.NumberInput(attrs={'size': 10}),
            'habilitación': forms.NumberInput(),
            'año_expediente': forms.NumberInput(attrs={'size': 5}),
            'número_expediente': forms.NumberInput(attrs={'size': 10}),
            'año_disposición': forms.NumberInput(attrs={'size': 5}),
            'número_disposición': forms.NumberInput(attrs={'size': 10}),
            'año_acuse': forms.NumberInput(attrs={'size': 5}),
            'acuse': forms.NumberInput(attrs={'size': 10}),
            'caja': forms.TextInput(),
            }

######################### Operador Nacional Radio ################################

class RadioNacionalForm(forms.ModelForm):
    class Meta:
        model = Operador_nacional_radio
        fields = '__all__'
        widgets = {
            'apellido': forms.TextInput(),
            'nombre': forms.TextInput(),
            'DNI': forms.NumberInput(),
            'año_formulario': forms.NumberInput(attrs={'size': 5}),
            'formulario': forms.NumberInput(attrs={'size': 10}),
            'año_dni': forms.NumberInput(attrs={'size': 5}),
            'pdf_dni': forms.NumberInput(attrs={'size': 10}),
            'secundario': forms.NumberInput(attrs={'size': 5}),
            'pdf_secundario': forms.NumberInput(attrs={'size': 10}),
            'instituto': forms.TextInput(),
            'año_instituto': forms.NumberInput(attrs={'size': 5}),
            'pdf_instituto': forms.NumberInput(attrs={'size': 10}),
            'año_acta': forms.NumberInput(attrs={'size': 5}),
            'acta': forms.NumberInput(attrs={'size': 10}),
            'habilitación': forms.NumberInput(),
            'año_expediente': forms.NumberInput(attrs={'size': 5}),
            'número_expediente': forms.NumberInput(attrs={'size': 10}),
            'año_disposición': forms.NumberInput(attrs={'size': 5}),
            'número_disposición': forms.NumberInput(attrs={'size': 10}),
            'año_acuse': forms.NumberInput(attrs={'size': 5}),
            'acuse': forms.NumberInput(attrs={'size': 10}),
            'caja': forms.TextInput(),
            }

######################### Operador Nacional TV ###################################

class TVNacionalForm(forms.ModelForm):
    class Meta:
        model = Operador_nacional_tv
        fields = '__all__'
        widgets = {
            'apellido': forms.TextInput(),
            'nombre': forms.TextInput(),
            'DNI': forms.NumberInput(),
            'año_formulario': forms.NumberInput(attrs={'size': 5}),
            'formulario': forms.NumberInput(attrs={'size': 10}),
            'año_dni': forms.NumberInput(attrs={'size': 5}),
            'pdf_dni': forms.NumberInput(attrs={'size': 10}),
            'secundario': forms.NumberInput(attrs={'size': 5}),
            'pdf_secundario': forms.NumberInput(attrs={'size': 10}),
            'instituto': forms.TextInput(),
            'año_instituto': forms.NumberInput(attrs={'size': 5}),
            'pdf_instituto': forms.NumberInput(attrs={'size': 10}),
            'año_acta': forms.NumberInput(attrs={'size': 5}),
            'acta': forms.NumberInput(attrs={'size': 10}),
            'habilitación': forms.NumberInput(),
            'año_expediente': forms.NumberInput(attrs={'size': 5}),
            'número_expediente': forms.NumberInput(attrs={'size': 10}),
            'año_disposición': forms.NumberInput(attrs={'size': 5}),
            'número_disposición': forms.NumberInput(attrs={'size': 10}),
            'año_acuse': forms.NumberInput(attrs={'size': 5}),
            'acuse': forms.NumberInput(attrs={'size': 10}),
            'caja': forms.TextInput(),
            }

######################### Operador Nacional Planta ###############################

class PlantaNacionalForm(forms.ModelForm):
    class Meta:
        model = Operador_nacional_planta
        fields = '__all__'
        widgets = {
            'apellido': forms.TextInput(),
            'nombre': forms.TextInput(),
            'DNI': forms.NumberInput(),
            'año_formulario': forms.NumberInput(attrs={'size': 5}),
            'formulario': forms.NumberInput(attrs={'size': 10}),
            'año_dni': forms.NumberInput(attrs={'size': 5}),
            'pdf_dni': forms.NumberInput(attrs={'size': 10}),
            'secundario': forms.NumberInput(attrs={'size': 5}),
            'pdf_secundario': forms.NumberInput(attrs={'size': 10}),
            'instituto': forms.TextInput(),
            'año_instituto': forms.NumberInput(attrs={'size': 5}),
            'pdf_instituto': forms.NumberInput(attrs={'size': 10}),
            'año_acta': forms.NumberInput(attrs={'size': 5}),
            'acta': forms.NumberInput(attrs={'size': 10}),
            'habilitación': forms.NumberInput(),
            'año_expediente': forms.NumberInput(attrs={'size': 5}),
            'número_expediente': forms.NumberInput(attrs={'size': 10}),
            'año_disposición': forms.NumberInput(attrs={'size': 5}),
            'número_disposición': forms.NumberInput(attrs={'size': 10}),
            'año_acuse': forms.NumberInput(attrs={'size': 5}),
            'acuse': forms.NumberInput(attrs={'size': 10}),
            'caja': forms.TextInput(),
            }

######################### Locutor Local ##########################################

class LocutorLocalForm(forms.ModelForm):
    class Meta:
        model = Locutor_local
        fields = '__all__'
        widgets = {
            'apellido': forms.TextInput(),
            'nombre': forms.TextInput(),
            'DNI': forms.NumberInput(),
            'año_formulario': forms.NumberInput(attrs={'size': 5}),
            'formulario': forms.NumberInput(attrs={'size': 10}),
            'año_dni': forms.NumberInput(attrs={'size': 5}),
            'pdf_dni': forms.NumberInput(attrs={'size': 10}),
            'secundario': forms.NumberInput(attrs={'size': 5}),
            'pdf_secundario': forms.NumberInput(attrs={'size': 10}),
            'localidad': forms.TextInput(),
            'provincia': forms.TextInput(),
            'año_certificado': forms.NumberInput(attrs={'size': 5}),
            'certificado': forms.NumberInput(attrs={'size': 10}),
            'año_acta': forms.NumberInput(attrs={'size': 5}),
            'acta': forms.NumberInput(attrs={'size': 10}),
            'habilitación': forms.NumberInput(),
            'año_expediente': forms.NumberInput(attrs={'size': 5}),
            'número_expediente': forms.NumberInput(attrs={'size': 10}),
            'año_disposición': forms.NumberInput(attrs={'size': 5}),
            'número_disposición': forms.NumberInput(attrs={'size': 10}),
            'año_acuse': forms.NumberInput(attrs={'size': 5}),
            'acuse': forms.NumberInput(attrs={'size': 10}),
            'caja': forms.TextInput(),
            }

######################### Operador Local Radio ###################################

class RadioLocalForm(forms.ModelForm):
    class Meta:
        model = Operador_local_radio
        fields = '__all__'
        widgets = {
            'apellido': forms.TextInput(),
            'nombre': forms.TextInput(),
            'DNI': forms.NumberInput(),
            'año_formulario': forms.NumberInput(attrs={'size': 5}),
            'formulario': forms.NumberInput(attrs={'size': 10}),
            'año_dni': forms.NumberInput(attrs={'size': 5}),
            'pdf_dni': forms.NumberInput(attrs={'size': 10}),
            'secundario': forms.NumberInput(attrs={'size': 5}),
            'pdf_secundario': forms.NumberInput(attrs={'size': 10}),
            'localidad': forms.TextInput(),
            'provincia': forms.TextInput(),
            'año_certificado': forms.NumberInput(attrs={'size': 5}),
            'certificado': forms.NumberInput(attrs={'size': 10}),
            'año_acta': forms.NumberInput(attrs={'size': 5}),
            'acta': forms.NumberInput(attrs={'size': 10}),
            'habilitación': forms.NumberInput(),
            'año_expediente': forms.NumberInput(attrs={'size': 5}),
            'número_expediente': forms.NumberInput(attrs={'size': 10}),
            'año_disposición': forms.NumberInput(attrs={'size': 5}),
            'número_disposición': forms.NumberInput(attrs={'size': 10}),
            'año_acuse': forms.NumberInput(attrs={'size': 5}),
            'acuse': forms.NumberInput(attrs={'size': 10}),
            'caja': forms.TextInput(),
            }

######################### Operador Local TV ######################################

class TVLocalForm(forms.ModelForm):
    class Meta:
        model = Operador_local_tv
        fields = '__all__'
        widgets = {
            'apellido': forms.TextInput(),
            'nombre': forms.TextInput(),
            'DNI': forms.NumberInput(),
            'año_formulario': forms.NumberInput(attrs={'size': 5}),
            'formulario': forms.NumberInput(attrs={'size': 10}),
            'año_dni': forms.NumberInput(attrs={'size': 5}),
            'pdf_dni': forms.NumberInput(attrs={'size': 10}),
            'secundario': forms.NumberInput(attrs={'size': 5}),
            'pdf_secundario': forms.NumberInput(attrs={'size': 10}),
            'localidad': forms.TextInput(),
            'provincia': forms.TextInput(),
            'año_certificado': forms.NumberInput(attrs={'size': 5}),
            'certificado': forms.NumberInput(attrs={'size': 10}),
            'año_acta': forms.NumberInput(attrs={'size': 5}),
            'acta': forms.NumberInput(attrs={'size': 10}),
            'habilitación': forms.NumberInput(),
            'año_expediente': forms.NumberInput(attrs={'size': 5}),
            'número_expediente': forms.NumberInput(attrs={'size': 10}),
            'año_disposición': forms.NumberInput(attrs={'size': 5}),
            'número_disposición': forms.NumberInput(attrs={'size': 10}),
            'año_acuse': forms.NumberInput(attrs={'size': 5}),
            'acuse': forms.NumberInput(attrs={'size': 10}),
            'caja': forms.TextInput(),
            }

######################### Operador Local Planta ##################################

class PlantaLocalForm(forms.ModelForm):
    class Meta:
        model = Operador_local_planta
        fields = '__all__'
        widgets = {
            'apellido': forms.TextInput(),
            'nombre': forms.TextInput(),
            'DNI': forms.NumberInput(),
            'año_formulario': forms.NumberInput(attrs={'size': 5}),
            'formulario': forms.NumberInput(attrs={'size': 10}),
            'año_dni': forms.NumberInput(attrs={'size': 5}),
            'pdf_dni': forms.NumberInput(attrs={'size': 10}),
            'secundario': forms.NumberInput(attrs={'size': 5}),
            'pdf_secundario': forms.NumberInput(attrs={'size': 10}),
            'localidad': forms.TextInput(),
            'provincia': forms.TextInput(),
            'año_certificado': forms.NumberInput(attrs={'size': 5}),
            'certificado': forms.NumberInput(attrs={'size': 10}),
            'año_acta': forms.NumberInput(attrs={'size': 5}),
            'acta': forms.NumberInput(attrs={'size': 10}),
            'habilitación': forms.NumberInput(),
            'año_expediente': forms.NumberInput(attrs={'size': 5}),
            'número_expediente': forms.NumberInput(attrs={'size': 10}),
            'año_disposición': forms.NumberInput(attrs={'size': 5}),
            'número_disposición': forms.NumberInput(attrs={'size': 10}),
            'año_acuse': forms.NumberInput(attrs={'size': 5}),
            'acuse': forms.NumberInput(attrs={'size': 10}),
            'caja': forms.TextInput(),
            }

######################### Productor ##############################################

class ProductorForm(forms.ModelForm):
    class Meta:
        model = Productor
        fields = '__all__'
        widgets = {
            'apellido': forms.TextInput(),
            'nombre': forms.TextInput(),
            'DNI': forms.NumberInput(),
            'año_formulario': forms.NumberInput(attrs={'size': 5}),
            'formulario': forms.NumberInput(attrs={'size': 10}),
            'año_dni': forms.NumberInput(attrs={'size': 5}),
            'pdf_dni': forms.NumberInput(attrs={'size': 10}),
            'secundario': forms.NumberInput(attrs={'size': 5}),
            'pdf_secundario': forms.NumberInput(attrs={'size': 10}),
            'instituto': forms.TextInput(),
            'año_instituto': forms.NumberInput(attrs={'size': 5}),
            'pdf_instituto': forms.NumberInput(attrs={'size': 10}),
            'año_acta': forms.NumberInput(attrs={'size': 5}),
            'acta': forms.NumberInput(attrs={'size': 10}),
            'habilitación': forms.NumberInput(),
            'año_expediente': forms.NumberInput(attrs={'size': 5}),
            'número_expediente': forms.NumberInput(attrs={'size': 10}),
            'año_disposición': forms.NumberInput(attrs={'size': 5}),
            'número_disposición': forms.NumberInput(attrs={'size': 10}),
            'año_acuse': forms.NumberInput(attrs={'size': 5}),
            'acuse': forms.NumberInput(attrs={'size': 10}),
            'caja': forms.TextInput(),
            }

######################### Guionista ##############################################

class GuionistaForm(forms.ModelForm):
    class Meta:
        model = Guionista
        fields = '__all__'
        widgets = {
            'apellido': forms.TextInput(),
            'nombre': forms.TextInput(),
            'DNI': forms.NumberInput(),
            'año_formulario': forms.NumberInput(attrs={'size': 5}),
            'formulario': forms.NumberInput(attrs={'size': 10}),
            'año_dni': forms.NumberInput(attrs={'size': 5}),
            'pdf_dni': forms.NumberInput(attrs={'size': 10}),
            'secundario': forms.NumberInput(attrs={'size': 5}),
            'pdf_secundario': forms.NumberInput(attrs={'size': 10}),
            'instituto': forms.TextInput(),
            'año_instituto': forms.NumberInput(attrs={'size': 5}),
            'pdf_instituto': forms.NumberInput(attrs={'size': 10}),
            'año_acta': forms.NumberInput(attrs={'size': 5}),
            'acta': forms.NumberInput(attrs={'size': 10}),
            'habilitación': forms.NumberInput(),
            'año_expediente': forms.NumberInput(attrs={'size': 5}),
            'número_expediente': forms.NumberInput(attrs={'size': 10}),
            'año_disposición': forms.NumberInput(attrs={'size': 5}),
            'número_disposición': forms.NumberInput(attrs={'size': 10}),
            'año_acuse': forms.NumberInput(attrs={'size': 5}),
            'acuse': forms.NumberInput(attrs={'size': 10}),
            'caja': forms.TextInput(),
            }
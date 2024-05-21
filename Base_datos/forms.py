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

class PersonaForm(forms.ModelForm):
    class Meta:
        widgets = {
            'apellido': forms.TextInput(),
            'nombre': forms.TextInput(),
            'DNI': forms.NumberInput(attrs={'class': 'input-large'}),
            'año_formulario': forms.NumberInput(attrs={'class': 'input-small'}),
            'formulario': forms.NumberInput(attrs={'class': 'input-large'}),
            'chequeo_formulario' : forms.CheckboxInput(),
            'año_dni': forms.NumberInput(attrs={'class': 'input-small'}),
            'pdf_dni': forms.NumberInput(attrs={'class': 'input-large'}),
            'chequeo_dni' : forms.CheckboxInput(),
            'secundario': forms.NumberInput(attrs={'class': 'input-small'}),
            'pdf_secundario': forms.NumberInput(attrs={'class': 'input-large'}),
            'chequeo_secu' : forms.CheckboxInput(),
            'año_acta': forms.NumberInput(attrs={'class': 'input-small'}),
            'acta': forms.NumberInput(attrs={'class': 'input-large'}),
            'habilitación': forms.NumberInput(),
            'año_expediente': forms.NumberInput(attrs={'class': 'input-small'}),
            'número_expediente': forms.NumberInput(attrs={'class': 'input-large'}),
            'chequeo_expediente': forms.CheckboxInput(),
            'año_disposición': forms.NumberInput(attrs={'class': 'input-small'}),
            'número_disposición': forms.NumberInput(attrs={'class': 'input-large'}),
            'año_acuse': forms.NumberInput(attrs={'class': 'input-small'}),
            'acuse': forms.NumberInput(attrs={'class': 'input-large'}),
            'caja': forms.TextInput(),
            # Para aspirantes Nacionales
            'instituto': forms.TextInput(),
            'año_instituto': forms.NumberInput(attrs={'class': 'input-small'}),
            'pdf_instituto': forms.NumberInput(attrs={'class': 'input-large'}),
            'chequeo_insti' : forms.CheckboxInput(),
            # Para aspirantes Locales
            'localidad': forms.TextInput(),
            'provincia': forms.TextInput(),
            'año_certificado': forms.NumberInput(attrs={'class': 'input-small'}),
            'certificado': forms.NumberInput(attrs={'class': 'input-large'}),
            'chequeo_certi' : forms.CheckboxInput(),
            }
        
    def __init__(self, *args, **kwargs):
        super(PersonaForm, self).__init__(*args, **kwargs)
        if not self.instance.inicio_tad:
            self.fields['inicio_tad'].widget = forms.DateInput(attrs={'type': 'date'})
        if not self.instance.reclamo_tad:
            self.fields['reclamo_tad'].widget = forms.DateInput(attrs={'type': 'date'})

######################### Locutor Nacional #######################################

class LocutorNacionalForm(PersonaForm):
    class Meta(PersonaForm.Meta):
        model = Locutor_nacional
        fields = '__all__'

######################### Operador Nacional Radio ################################

class RadioNacionalForm(PersonaForm):
    class Meta(PersonaForm.Meta):
        model = Operador_nacional_radio
        fields = '__all__'

######################### Operador Nacional TV ###################################

class TVNacionalForm(PersonaForm):
    class Meta(PersonaForm.Meta):
        model = Operador_nacional_tv
        fields = '__all__'

######################### Operador Nacional Planta ###############################

class PlantaNacionalForm(PersonaForm):
    class Meta(PersonaForm.Meta):
        model = Operador_nacional_planta
        fields = '__all__'

######################### Locutor Local ##########################################

class LocutorLocalForm(PersonaForm):
    class Meta(PersonaForm.Meta):
        model = Locutor_local
        fields = '__all__'

######################### Operador Local Radio ###################################

class RadioLocalForm(PersonaForm):
    class Meta(PersonaForm.Meta):
        model = Operador_local_radio
        fields = '__all__'

######################### Operador Local TV ######################################

class TVLocalForm(PersonaForm):
    class Meta(PersonaForm.Meta):
        model = Operador_local_tv
        fields = '__all__'

######################### Operador Local Planta ##################################

class PlantaLocalForm(PersonaForm):
    class Meta(PersonaForm.Meta):
        model = Operador_local_planta
        fields = '__all__'

######################### Productor ##############################################

class ProductorForm(PersonaForm):
    class Meta(PersonaForm.Meta):
        model = Productor
        fields = '__all__'

######################### Guionista ##############################################

class GuionistaForm(PersonaForm):
    class Meta(PersonaForm.Meta):
        model = Guionista
        fields = '__all__'
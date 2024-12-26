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
            'apellido': forms.TextInput(attrs={'class': 'form-control-sm input-large'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control-sm input-large'}),
            'DNI': forms.NumberInput(attrs={'class': 'form-control-sm input-medium'}),
            'año_formulario': forms.NumberInput(attrs={'class': 'form-control-sm input-small'}),
            'formulario': forms.NumberInput(attrs={'class': 'form-control-sm input-medium'}),
            'chequeo_formulario' : forms.CheckboxInput(),
            'año_dni': forms.NumberInput(attrs={'class': 'form-control-sm input-small'}),
            'pdf_dni': forms.NumberInput(attrs={'class': 'form-control-sm input-medium'}),
            'chequeo_dni' : forms.CheckboxInput(),
            'secundario': forms.NumberInput(attrs={'class': 'form-control-sm input-small'}),
            'pdf_secundario': forms.NumberInput(attrs={'class': 'form-control-sm input-medium'}),
            'chequeo_secu' : forms.CheckboxInput(),
            'año_acta': forms.NumberInput(attrs={'class': 'form-control-sm input-small'}),
            'acta': forms.NumberInput(attrs={'class': 'form-control-sm input-medium'}),
            'habilitación': forms.NumberInput(attrs={'class': 'form-control-sm input-medium'}),
            'año_expediente': forms.NumberInput(attrs={'class': 'form-control-sm input-small'}),
            'número_expediente': forms.NumberInput(attrs={'class': 'form-control-sm input-medium'}),
            'chequeo_expediente': forms.CheckboxInput(),
            'año_disposición': forms.NumberInput(attrs={'class': 'form-control-sm input-small'}),
            'número_disposición': forms.NumberInput(attrs={'class': 'form-control-sm input-large'}),
            'año_acuse': forms.NumberInput(attrs={'class': 'form-control-sm input-small'}),
            'acuse': forms.NumberInput(attrs={'class': 'form-control-sm input-medium'}),
            'caja': forms.TextInput(attrs={'class': 'form-control-sm input-medium'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control w-100', 'rows':3, 'cols': 100}),
            # Para aspirantes Nacionales
            'instituto': forms.TextInput(attrs={'class': 'form-control-sm input-large'}),
            'año_instituto': forms.NumberInput(attrs={'class': 'form-control-sm input-small'}),
            'pdf_instituto': forms.NumberInput(attrs={'class': 'form-control-sm input-medium'}),
            'chequeo_insti' : forms.CheckboxInput(),
            # Para aspirantes Locales
            'localidad': forms.TextInput(attrs={'class': 'form-control-sm input large'}),
            'provincia': forms.TextInput(attrs={'class': 'form-control-sm input large'}),
            'año_certificado': forms.NumberInput(attrs={'class': 'form-control-sm input-small'}),
            'certificado': forms.NumberInput(attrs={'class': 'form-control-sm input-medium'}),
            'chequeo_certi' : forms.CheckboxInput(),
            }

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
    
    def __init__(self, *args, **kwargs):
        super(PersonaForm, self).__init__(*args, **kwargs)
        if not self.instance.inicio_tad:
            self.fields['inicio_tad'].widget = forms.DateInput(attrs={'class': 'form-control-sm', 'type': 'date'})
        if not self.instance.reclamo_tad:
            self.fields['reclamo_tad'].widget = forms.DateInput(attrs={'class': 'form-control-sm', 'type': 'date'})

######################### Operador Local Radio ###################################

class RadioLocalForm(PersonaForm):
    class Meta(PersonaForm.Meta):
        model = Operador_local_radio
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PersonaForm, self).__init__(*args, **kwargs)
        if not self.instance.inicio_tad:
            self.fields['inicio_tad'].widget = forms.DateInput(attrs={'class': 'form-control-sm', 'type': 'date'})
        if not self.instance.reclamo_tad:
            self.fields['reclamo_tad'].widget = forms.DateInput(attrs={'class': 'form-control-sm', 'type': 'date'})

######################### Operador Local TV ######################################

class TVLocalForm(PersonaForm):
    class Meta(PersonaForm.Meta):
        model = Operador_local_tv
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PersonaForm, self).__init__(*args, **kwargs)
        if not self.instance.inicio_tad:
            self.fields['inicio_tad'].widget = forms.DateInput(attrs={'class': 'form-control-sm', 'type': 'date'})
        if not self.instance.reclamo_tad:
            self.fields['reclamo_tad'].widget = forms.DateInput(attrs={'class': 'form-control-sm', 'type': 'date'})

######################### Operador Local Planta ##################################

class PlantaLocalForm(PersonaForm):
    class Meta(PersonaForm.Meta):
        model = Operador_local_planta
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PersonaForm, self).__init__(*args, **kwargs)
        if not self.instance.inicio_tad:
            self.fields['inicio_tad'].widget = forms.DateInput(attrs={'class': 'form-control-sm', 'type': 'date'})
        if not self.instance.reclamo_tad:
            self.fields['reclamo_tad'].widget = forms.DateInput(attrs={'class': 'form-control-sm', 'type': 'date'})

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
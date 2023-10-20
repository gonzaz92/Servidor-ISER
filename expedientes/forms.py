from django import forms
from .models import Expediente, categorias

class ExpedienteForm(forms.ModelForm):
    class Meta:
        model = Expediente
        fields = '__all__'
        categorias
        widgets = {
            'Fecha_de_Creación': forms.DateInput(attrs={'type': 'date'}),
            'Fecha_de_disposición': forms.DateInput(attrs={'type': 'date'}),
            'Año_de_Expediente': forms.NumberInput(attrs={'size': 5})
        }

class ExpedienteUpdate(forms.ModelForm):
    class Meta:
        model = Expediente
        fields = '__all__'
        widgets = {
            'Fecha_de_disposición': forms.DateInput(attrs={'type': 'date'}),
            'Año_de_Expediente': forms.NumberInput(attrs={'size': 5})
        }
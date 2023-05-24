from django import forms
from .models import Expediente

class ExpedienteForm(forms.ModelForm):
    class Meta:
        model = Expediente
        fields = '__all__'
        widgets = {
            'Fecha_de_Creación': forms.DateInput(attrs={'type': 'date'}),
            'Fecha_de_disposición': forms.DateInput(attrs={'type': 'date'}),
        }

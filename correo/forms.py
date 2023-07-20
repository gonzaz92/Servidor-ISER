from django import forms
from .models import Correo

class CorreoForm(forms.ModelForm):
    class Meta:
        model = Correo
        fields = '__all__'
        widgets = {
            'envio': forms.DateInput(attrs={'type': 'date'}),
        }

from django import forms
from .models import Correo

class CorreoForm(forms.ModelForm):
    class Meta:
        model = Correo
        fields = '__all__'
        widgets = {
            'envio': forms.DateInput(attrs={'type': 'date'}),
            'destinatario': forms.TextInput(),
            'nombre': forms.TextInput(),
            'dni': forms.NumberInput(),
            'carnet': forms.NumberInput(),
            'direccion': forms.TextInput(),
            'localidad': forms.TextInput(),
            'provincia': forms.TextInput(),
            'seguimiento': forms.TextInput(),
            'categoria': forms.Select(),
            'telefono': forms.TextInput(),
            'mail': forms.TextInput(),
            'observaciones': forms.Textarea(attrs={'rows': 2, 'cols': 18}),
            'año_acuse': forms.NumberInput(attrs={'size': 5}),
            'acuse': forms.TextInput(),
        }

class CorreoUpdate(forms.ModelForm):
    class Meta:
        model = Correo
        fields = '__all__'
        widgets = {
            'destinatario': forms.TextInput(),
            'nombre': forms.TextInput(),
            'dni': forms.NumberInput(),
            'carnet': forms.NumberInput(),
            'direccion': forms.TextInput(),
            'localidad': forms.TextInput(),
            'provincia': forms.TextInput(),
            'seguimiento': forms.TextInput(),
            'categoria': forms.Select(),
            'telefono': forms.TextInput(),
            'mail': forms.TextInput(),
            'observaciones': forms.Textarea(attrs={'rows': 2, 'cols': 18}),
            'año_acuse': forms.NumberInput(attrs={'size': 5}),
            'acuse': forms.TextInput(),
        }
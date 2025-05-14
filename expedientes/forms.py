from django import forms
from .models import Expediente

class ExpedienteForm(forms.ModelForm):
    class Meta:
        model = Expediente
        fields = '__all__'
        widgets = {
            'fecha_asignado': forms.DateInput(attrs={'type': 'date'}),
            'Fecha_de_Creación': forms.DateInput(attrs={'type': 'date'}),
            'fecha_pase': forms.DateInput(attrs={'type': 'date'}),
            'Fecha_de_disposición': forms.DateInput(attrs={'type': 'date'}),
            'Año_de_Expediente': forms.NumberInput(attrs={'class': 'input-small'}),
            'observaciones': forms.Textarea(attrs={'rows': 3, 'cols': 100}),
        }

class ExpedienteUpdate(forms.ModelForm):
    class Meta:
        model = Expediente
        fields = '__all__'
        widgets = {
            'observaciones': forms.Textarea(attrs={'rows': 3, 'cols': 100}),
        }

    def __init__(self, *args, **kwargs):
        super(ExpedienteUpdate, self).__init__(*args, **kwargs)
        self.fields['Año_de_Expediente'].widget.attrs['class'] = 'input-small'
        if not self.instance.Fecha_de_disposición:
            self.fields['Fecha_de_disposición'].widget = forms.DateInput(attrs={'type': 'date'})
        if not self.instance.fecha_pase:
            self.fields['fecha_pase'].widget = forms.DateInput(attrs={'type': 'date'})
        if not self.instance.pase_legal:
            self.fields['pase_legal'].widget = forms.DateInput(attrs={'type': 'date'})
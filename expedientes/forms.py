from django import forms
from .models import Expediente

class ExpedienteForm(forms.ModelForm):
    class Meta:
        model = Expediente
        fields = '__all__'
        widgets = {
            'Fecha_de_Creación': forms.DateInput(attrs={'type': 'date'}),
            'Fecha_de_disposición': forms.DateInput(attrs={'type': 'date'}),
            'Año_de_Expediente': forms.NumberInput(attrs={'class': 'input-small'})
        }

class ExpedienteUpdate(forms.ModelForm):
    class Meta:
        model = Expediente
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ExpedienteUpdate, self).__init__(*args, **kwargs)
        self.fields['Año_de_Expediente'].widget.attrs['class'] = 'input-small'
        if not self.instance.Fecha_de_disposición:
            self.fields['Fecha_de_disposición'].widget = forms.DateInput(attrs={'type': 'date'})
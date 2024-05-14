from django import forms
from .models import Acta, Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'
        widgets = {
            'nombre' : forms.TextInput(attrs={'class': 'form-control mb-3', 'size' : '100%'}),
        }

class ActaForm(forms.ModelForm):
    class Meta:
        model = Acta
        fields = '__all__'
        widgets = {
            'instituto' : forms.TextInput(attrs={'size':'60%'}),
            'fecha' : forms.DateInput(attrs={'type':'date'}),
            'profesores' : forms.TextInput(attrs={'size': '114%'}),
            'persona1' : forms.TextInput(attrs={'size': '60%'}),
            'persona2' : forms.TextInput(attrs={'size': '60%'}),
            'persona3' : forms.TextInput(attrs={'size': '60%'}),
            'persona4' : forms.TextInput(attrs={'size': '60%'}),
            'persona5' : forms.TextInput(attrs={'size': '60%'}),
            'persona6' : forms.TextInput(attrs={'size': '60%'}),
            'persona7' : forms.TextInput(attrs={'size': '60%'}),
            'persona8' : forms.TextInput(attrs={'size': '60%'}),
            'persona9' : forms.TextInput(attrs={'size': '60%'}),
            'persona10' : forms.TextInput(attrs={'size': '60%'}),
            'persona11' : forms.TextInput(attrs={'size': '60%'}),
            'persona12' : forms.TextInput(attrs={'size': '60%'}),
            'persona13' : forms.TextInput(attrs={'size': '60%'}),
            'persona14' : forms.TextInput(attrs={'size': '60%'}),
            'persona15' : forms.TextInput(attrs={'size': '60%'}),
            'persona16' : forms.TextInput(attrs={'size': '60%'}),
            'persona17' : forms.TextInput(attrs={'size': '60%'}),
            'persona18' : forms.TextInput(attrs={'size': '60%'}),
            'persona19' : forms.TextInput(attrs={'size': '60%'}),
            'persona20' : forms.TextInput(attrs={'size': '60%'}),
            'persona21' : forms.TextInput(attrs={'size': '60%'}),
            'persona22' : forms.TextInput(attrs={'size': '60%'}),
            'persona23' : forms.TextInput(attrs={'size': '60%'}),
            'persona24' : forms.TextInput(attrs={'size': '60%'}),
            'persona25' : forms.TextInput(attrs={'size': '60%'}),
            'firma1' : forms.TextInput(attrs={'size': '60%'}),
            'firma2' : forms.TextInput(attrs={'size': '60%'}),
            'firma3' : forms.TextInput(attrs={'size': '60%'}),
        }

    def __init__(self, *args, **kwargs):
        super(ActaForm, self).__init__(*args, **kwargs)
        if not self.instance.fecha:
            self.fields['fecha'].widget = forms.DateInput(attrs={'type': 'date'})
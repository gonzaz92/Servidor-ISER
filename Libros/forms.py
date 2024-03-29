from django import forms
from .models import Acta, Libro

# from django.contrib import admin


class ActaForm(forms.ModelForm):
    class Meta:
        model = Acta
        fields = '__all__'
        widgets = {
            # 'instituto' : AutocompleteSelect(
            #     Acta._meta.get_field('instituto').remote_field,
            #     admin.site, 
            #     attrs={'placeholder' : 'selecionar...'}),
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
        }

class ActaUpdate(forms.ModelForm):
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
        }

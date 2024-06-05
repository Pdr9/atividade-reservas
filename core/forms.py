import datetime
from django.forms import ModelForm
from django import forms
from .models import Reserva

class ReservaForm(ModelForm):

    class Meta:
        model = Reserva
        fields = '__all__'
        widgets = {
            'cnpj' : forms.TextInput(attrs={'class': 'form-control' }),
            'name' : forms.TextInput(attrs={'class': 'form-control' }),
            'category' : forms.TextInput(attrs={'class': 'form-control' }),
            'quitado': forms.CheckboxInput(attrs={'class': 'form-group', 'style': 'display: flex'}),


            'stand' : forms.Select(attrs={'class': 'form-control'}),
        }

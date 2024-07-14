from django import forms
from .models import Autor


class AutorForms(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['name',
    'second_name', 
    'email', 
    'bio',  
    'bday' ]

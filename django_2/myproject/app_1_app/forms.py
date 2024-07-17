from django import forms
from .models import Product


class UserForm(forms.Form):
    name = forms.CharField(max_length = 100)
    email = forms.EmailField()
    password = forms.CharField(max_length = 100)
    age = forms.IntegerField()


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'quaniti','image']     
from tkinter import Widget
from django import forms
from .models import Contacto, Producto
from django.contrib.auth.forms import UserCreationForm

class ContactoForm(forms.ModelForm):

    #nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model = Contacto
        #fields = ["nombre", "correo" , "tipo_consulta", "mensaje", "avisos"]
        fields = '__all__'

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

        Widgets = {
            "fecha_fabricacion": forms.SelectDateWidget()
        }

class CustomUserCreationForm(UserCreationForm):
    pass 
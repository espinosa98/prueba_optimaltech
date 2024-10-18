
# Django
from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['descripcion']
        labels = {
            'descripcion': 'Descripción'
        }
        widgets = {
            'descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la descripción del producto'
                }
            )
        }

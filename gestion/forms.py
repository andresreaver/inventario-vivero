from django import forms
from gestion.models.proveedor import Proveedor
from gestion.models.cliente import Cliente

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = [
            'nombre_razon_social',
            'nit_cedula',
            'tipo_documento',
            'telefono',
            'correo_electronico',
            'direccion',
        ]
        widgets = {
            'nombre_razon_social': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre o razón social'}),
            'nit_cedula': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el NIT o Cédula'}),
            'tipo_documento': forms.Select(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el teléfono'}),
            'correo_electronico': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el correo electrónico'}),
            'direccion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese la dirección', 'rows': 3}),
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nombre_razon_social',
            'nit_cedula',
            'tipo_documento',
            'telefono',
            'correo_electronico',
            'direccion',
        ]
        widgets = {
            'nombre_razon_social': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre o razón social'}),
            'nit_cedula': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el NIT o Cédula'}),
            'tipo_documento': forms.Select(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el teléfono'}),
            'correo_electronico': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el correo electrónico'}),
            'direccion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese la dirección', 'rows': 3}),
        }

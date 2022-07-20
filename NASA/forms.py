from django import forms

from .models import Usuario

class UsuarioForm(forms.Form):
    nombre = forms.CharField(label="Nombre",max_length=45, required=True)
    cedula = forms.CharField(label="Cedula", max_length=45, required=True)
    apellidos = forms.CharField(label="Apellidos", max_length=45)
    direccion = forms.CharField(label="Direccion", max_length=10)
    telefono = forms.CharField(label="Telefono", max_length=10)
    correo = forms.CharField(label="Correo", max_length=10)
    tipo_usuario = forms.CharField(label="Tipo usuario", max_length=10)
    contrasena = forms.CharField(label="Contraseña", max_length=10)
    estado = forms.CharField(label="Estado", max_length=10)

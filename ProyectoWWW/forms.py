from django import forms

from .models import Usuarios

class UsuarioForm(forms.Form):
    nombre_usuario = forms.CharField(label="Nombre Usuario",max_length=45, required=True)
    paterno_usuario = forms.CharField(label="Primer apellido", max_length=45, required=True)
    materno_usuario = forms.CharField(label="Segundo apellido", max_length=45)
    rol_usuario = forms.CharField(label="Seleccione Rol", max_length=10)
    correo_usuario = forms.EmailField(label="Correo", max_length=70, null=True, unique=True, required=True)
    contrasena_usuario = forms.PasswordInput(label="Contraseña", max_length=90, required=True)
from typing import Optional
from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    nombre = models.CharField(max_length=50)
    cedula = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    tipo_usuario = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)




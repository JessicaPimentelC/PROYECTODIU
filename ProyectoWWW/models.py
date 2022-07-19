from typing import Optional
from django.db import models

class Usuarios(models.Model):
    ID_usuario = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    nombre_usuario = models.CharField(max_length=45)
    paterno_usuario = models.CharField(max_length=45)
    materno_usuario = models.CharField(null = True, max_length=45)
    rol_usuario = models.CharField(max_length=20)
    correo_usuario = models.EmailField(max_length=70, blank=True, null=True, unique=True)
    contrasena_usuario = models.CharField(max_length=90)

class Proveedores(models.Model):
    ID_proveedor = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    nombre_proveedor = models.CharField(max_length=45)
    direccion_proveedor = models.CharField(max_length=20)
    celular_proveedor = models.CharField(max_length=45)
    encargado_proveedor = models.CharField(max_length=45)
    correo_proveedor = models.EmailField(max_length=70, blank=True, null=True, unique=True)

class Inventario(models.Model):
    ID_item = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    proveedor_ID_item=models.ForeignKey(Proveedores,related_name='Provee_inventario',on_delete=models.CASCADE)
    nombre_item = models.CharField(max_length=45)
    cantidad_item = models.IntegerField()
    referencia_item = models.CharField(max_length=45)
    estado_item = models.CharField(max_length=45)
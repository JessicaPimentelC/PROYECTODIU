from typing import Optional
from typing_extensions import Required
from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    nombre = models.CharField(max_length=50)
    cedula = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    correo = models.EmailField(max_length=50)
    tipo_usuario = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
 
class Ventas_almacen(models.Model):
    id_ventas_a = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    id_zapatillas_a = models.IntegerField(null=True)
    id_zapatillas_n = models.IntegerField(null=True)
    talla = models.IntegerField()
    precio_venta = models.IntegerField()
    fecha_venta = models.DateField()
    
class Ventas_linea(models.Model):
    id_ventas_l = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    id_zapatillas_a = models.IntegerField()
    id_zapatillas_n = models.IntegerField()
    talla = models.IntegerField()
    precio_venta = models.IntegerField()
    fecha_venta = models.DateField()


class Zapatillas_a_almacen(models.Model):
    id_zap_a_almacen = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    estilo = models.CharField(max_length=50)
    precio_compra = models.IntegerField()
    proveedor = models.CharField(max_length=50)
    talla_43 = models.IntegerField()
    talla_42 = models.IntegerField()
    talla_41 = models.IntegerField()
    talla_40 = models.IntegerField()
    talla_39 = models.IntegerField()
    talla_38 = models.IntegerField()
    talla_37 = models.IntegerField()
    talla_36 = models.IntegerField()
    talla_35 = models.IntegerField()
    talla_34 = models.IntegerField()
    talla_33 = models.IntegerField()

class Zapatillas_a_linea(models.Model):
    id_zap_a_linea = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    estilo = models.CharField(max_length=50)
    precio_compra = models.IntegerField()
    proveedor = models.CharField(max_length=50)
    talla_43 = models.IntegerField()
    talla_42 = models.IntegerField()
    talla_41 = models.IntegerField()
    talla_40 = models.IntegerField()
    talla_39 = models.IntegerField()
    talla_38 = models.IntegerField()
    talla_37 = models.IntegerField()
    talla_36 = models.IntegerField()
    talla_35 = models.IntegerField()
    talla_34 = models.IntegerField()
    talla_33 = models.IntegerField()

class Zapatillas_n_almacen(models.Model):
    id_zap_n_almacen = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    estilo = models.CharField(max_length=50)
    precio_compra = models.IntegerField()
    proveedor = models.CharField(max_length=50)
    talla_32 = models.IntegerField()
    talla_31 = models.IntegerField()
    talla_30 = models.IntegerField()
    talla_29 = models.IntegerField()
    talla_28 = models.IntegerField()
    talla_27 = models.IntegerField()
    talla_26 = models.IntegerField()
    talla_25 = models.IntegerField()
    talla_24 = models.IntegerField()
    talla_23 = models.IntegerField()
    talla_22 = models.IntegerField()

class Zapatillas_n_linea(models.Model):
    id_zap_n_linea = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    estilo = models.CharField(max_length=50)
    precio_compra = models.IntegerField()
    proveedor = models.CharField(max_length=50)
    talla_32 = models.IntegerField()
    talla_31 = models.IntegerField()
    talla_30 = models.IntegerField()
    talla_29 = models.IntegerField()
    talla_28 = models.IntegerField()
    talla_27 = models.IntegerField()
    talla_26 = models.IntegerField()
    talla_25 = models.IntegerField()
    talla_24 = models.IntegerField()
    talla_23 = models.IntegerField()
    talla_22 = models.IntegerField()

class Gastos_Variable_almacen(models.Model):
    id_gasto_variable_a = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    costo = models.IntegerField()
    fecha = models.DateField()
    descripcion = models.CharField(max_length=200)
    
class Gastos_Variable_linea(models.Model):
    id_gasto_variable_l = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    costo = models.IntegerField()
    fecha = models.DateField()
    descripcion = models.CharField(max_length=200)

class Gastos_Fijos_Almacen(models.Model):
    id_gasto_variable_l = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    costo = models.IntegerField()
    fecha = models.DateField()
    descripcion = models.CharField(max_length=200)
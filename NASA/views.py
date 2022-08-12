from cgi import print_environ
from cmath import cos, pi
from email.policy import default
from typing_extensions import Required
from django.db.models.query import EmptyQuerySet
from django.forms import EmailField
from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
from datetime import datetime



# Conexión a la base de datos 
from . import models
Usuario = models.Usuario
Zapatilla_a_almacen = models.Zapatillas_a_almacen
Zapatilla_n_almacen = models.Zapatillas_n_almacen
Zapatilla_a_linea = models.Zapatillas_a_linea
Zapatilla_n_linea = models.Zapatillas_n_linea
Ventas_almacen = models.Ventas_almacen
Gastos_Variable_almacen = models.Gastos_Variable_almacen
Gastos_Fijos_Almacen = models.Gastos_Fijos_Almacen
Gastos_Variable_linea = models.Gastos_Variable_linea
Ventas_linea = models.Ventas_linea
GastosVariable_Almacen = models.Gastos_Variable_almacen
GastosVariable_Linea = models.Gastos_Variable_linea

def index(request):
    # Post enviado desde formulario en login
    print(request.POST)

    email = request.POST['user_email']
    password = request.POST['user_password']
    
    usuario_db = Usuario.objects.filter(correo = email)
    # usuario con correo igual
    print(usuario_db)
    print(len(usuario_db))
    if len(usuario_db) == 0:
        # No existe el correo ingresado en la base de datos
        
        return render(request, "login.html")
    
    datos = usuario_db.get()

    password_db = datos.contrasena
    rol_db = datos.tipo_usuario
    estado_db = datos.estado

    if password == password_db:
        if rol_db == "Admin" and estado_db=="Activo" :
            return render(request, "InterfazAdmin.html")

        if rol_db == "Empleado" and estado_db=="Activo":
            return render(request, "InterfazEmpleado.html")
    else:
      #Contraseña incorrecta  
       
        return render(request, "login.html")        
    # aqui no debería llegar pero dejo el return por cuestiones de evitar errores
    return render(request, "login.html")

def login(request):
    return render(request, "login.html")

def registro(request):
    return render(request, "register.html")

def registroMateriales(request):
    return render(request, "registroMateriales.html")

def crearProveedores(request):
    return render(request, "registrarProveedores.html")

def verInventario(request):
    return render(request, "verInventario.html")

def verProveedores(request):
    return render(request, "verProveedores.html")

def verSolicitudesMateriales(request):
    return render(request, "verSolicitudesMateriales.html")

def solicitarMateriales(request):
    return render(request, "solicitarMateriales.html")

def solicitarMaterialesObra(request):
    return render(request, "solicitarMaterialesObra.html")

def interfazJefeAlmacen(request):
    return render(request, "interfazJefeAlmacen.html")

def gestionZapatillas(request):
    return render(request, "GestionZapatillas.html")

def gestionZapatillasEL(request):
    return render(request, "GestionZapatillasEL.html")
   
def gestionPedidos(request):
    return render(request, "GestionPedidos.html")

def gestionPedidosEL(request):
    return render(request, "GestionPedidosEL.html")

def gestionVentas(request):
    return render(request, "GestionVentas.html")

def gestionVentasEL(request):
    return render(request, "GestionVentasEL.html")

def gestionGastos(request):
    return render(request, "GestionGastos.html")

def gestionGastosEL(request):
    return render(request, "GestionGastosEL.html")

def interfazJefeObra(request):
    return render(request, "interfazJefeObra.html")

def forgotPassword(request):
    return render(request, "forgot-password.html")

def error404(request):
    return render(request, "404.html")

def blank(request):
    return render(request, "blank.html")

def buttons(request):
    return render(request, "buttons.html")

def cards(request):
    return render(request, "cards.html")

def charts(request):
    return render(request, "charts.html")

def tables(request):
    return render(request, "tables.html")

def utilitiesAnimation(request):
    return render(request, "utilities-animation.html")

def utilitiesBorder(request):
    return render(request, "utilities-border.html")

def utilitiesColor(request):
    return render(request, "utilities-color.html")

def utilitiesOther(request):
    return render(request, "utilities-other.html")

def solicitudObras(request):
    return render(request, "SolicitudObras.html")

def crearCliente(request):
    return render(request, "CrearCliente.html")

def modificarCliente(request):
    return render(request, "ModificarCliente.html")

def eliminarCliente(request):
    return render(request, "EliminarCliente.html")

def listaCliente(request):
    return render(request, "listaCliente.html")

def verUsuario(request):
    return render(request, "verUsuario.html")

def crearVenta(request):
    mensaje = ""

    if request.method == "POST":
        print("primer if")
        zapatillas_a_alm = request.POST['id_zapatillas_a']
        zapatillas_n_alm = request.POST['id_zapatillas_n']
        talla = request.POST['talla']
        precio_venta = request.POST['precio_venta']
        fecha_venta = request.POST['fecha_venta']

        if (len(zapatillas_a_alm) !=0):
            u = Ventas_almacen(id_zapatillas_a = zapatillas_a_alm, id_zapatillas_n=zapatillas_n_alm,talla=talla, precio_venta=precio_venta, fecha_venta = fecha_venta)    
            u.save()
            restaInventarioZap_aA(request,talla,zapatillas_a_alm)
            restaInventarioZap_nA(request,talla,zapatillas_n_alm)
            mensaje = "guardado exitosamente"
    return render(request, "CrearVenta.html", {"mensaje":mensaje})

def crearVentaEL(request):
    mensaje = ""
    if request.method == "POST":
        zapatillas_a_lin = request.POST['id_zapatillas_a']
        zapatillas_n_lin = request.POST['id_zapatillas_n']
        talla = request.POST['talla']
        precio_venta = request.POST['precio_venta']
        fecha_venta = request.POST['fecha_venta']

        if len(zapatillas_a_lin) !=0:
            u = Ventas_linea(id_zapatillas_a = zapatillas_a_lin, id_zapatillas_n=zapatillas_n_lin,talla=talla, precio_venta=precio_venta, fecha_venta = fecha_venta)    
            u.save()
            restaInventarioZap_nL(request,talla,zapatillas_n_lin)
            mensaje = "guardado exitosamente"
    return render(request, "CrearVentaEL.html", {"mensaje":mensaje})

def restaInventarioZap_aA(request,tallap,codZapA):

    dismin = Zapatilla_a_almacen.objects.get(id_zap_a_almacen=codZapA)
    if tallap == "33":
        dismin.talla_33 -= 1
    elif tallap == "34":
        dismin.talla_34 -= 1
    elif tallap == "35":
        dismin.talla_35 -= 1
    elif tallap == "36":
        dismin.talla_36 -= 1
    elif tallap == "37":
        dismin.talla_37 -= 1
    elif tallap == "38":
        dismin.talla_38 -= 1
    elif tallap == "39":
        dismin.talla_39 -= 1
    elif tallap == "40":
        dismin.talla_40 -= 1
    elif tallap == "41":
        dismin.talla_41 -= 1
    elif tallap == "42":
        dismin.talla_42 -= 1
    elif tallap == "43":
        dismin.talla_43 -= 1                        
    dismin.save()
                                
    return render(request, "CrearVenta.html",{dismin:dismin})

def restaInventarioZap_nA(request,tallap,codZapN):

    dismin = Zapatilla_n_almacen.objects.get(id_zap_n_almacen=codZapN)
    if tallap == "32":
        dismin.talla_32 -= 1
    elif tallap == "31":
        dismin.talla_31 -= 1
    elif tallap == "30":
        dismin.talla_30 -= 1
    elif tallap == "29":
        dismin.talla_29 -= 1
    elif tallap == "28":
        dismin.talla_28 -= 1
    elif tallap == "27":
        dismin.talla_27 -= 1
    elif tallap == "26":
        dismin.talla_26 -= 1
    elif tallap == "25":
        dismin.talla_25 -= 1
    elif tallap == "24":
        dismin.talla_24 -= 1
    elif tallap == "23":
        dismin.talla_23 -= 1
    elif tallap == "22":
        dismin.talla_22 -= 1                        
    dismin.save()
                                
    return render(request, "CrearVenta.html",{dismin:dismin})

def restaInventarioZap_aL(request,tallap,codZapA):
    
    dismin = Zapatilla_a_linea.objects.get(id_zap_a_linea=codZapA)
    if tallap == "33":
        dismin.talla_33 -= 1
    elif tallap == "34":
        dismin.talla_34 -= 1
    elif tallap == "35":
        dismin.talla_35 -= 1
    elif tallap == "36":
        dismin.talla_36 -= 1
    elif tallap == "37":
        dismin.talla_37 -= 1
    elif tallap == "38":
        dismin.talla_38 -= 1
    elif tallap == "39":
        dismin.talla_39 -= 1
    elif tallap == "40":
        dismin.talla_40 -= 1
    elif tallap == "41":
        dismin.talla_41 -= 1
    elif tallap == "42":
        dismin.talla_42 -= 1
    elif tallap == "43":
        dismin.talla_43 -= 1                        
    dismin.save()
                                
    return render(request, "CrearVenta.html",{dismin:dismin})

def restaInventarioZap_nL(request,tallap,codZapN):

    dismin = Zapatilla_n_linea.objects.get(id_zap_n_linea=codZapN)
    if tallap == "32":
        dismin.talla_32 -= 1
    elif tallap == "31":
        dismin.talla_31 -= 1
    elif tallap == "30":
        dismin.talla_30 -= 1
    elif tallap == "29":
        dismin.talla_29 -= 1
    elif tallap == "28":
        dismin.talla_28 -= 1
    elif tallap == "27":
        dismin.talla_27 -= 1
    elif tallap == "26":
        dismin.talla_26 -= 1
    elif tallap == "25":
        dismin.talla_25 -= 1
    elif tallap == "24":
        dismin.talla_24 -= 1
    elif tallap == "23":
        dismin.talla_23 -= 1
    elif tallap == "22":
        dismin.talla_22 -= 1                        
    dismin.save()
                                
    return render(request, "CrearVenta.html",{dismin:dismin})
def eliminarZapatilla_a_A(request, zapatillas_a_alm):
    proveedor = Ventas_almacen.objects.filter(id_zapatillas_a=zapatillas_a_alm)
    proveedor.delete()
    return render(request, "CrearVenta.html",{proveedor:proveedor})

def consultarVenta(request):
    mensaje = ""
    id_zapatillas_a =""
    id_zapatillas_n = ""
    talla = ""
    precio_venta = ""
    fecha_venta = ""
    
    if request.method == "POST":
        fecha = request.POST['precio_venta']
        if len(fecha) !=0:            
            u = Ventas_almacen.objects.filter(precio_venta=fecha)   
            if len(u) == 1:
                datos = u.get()
                id_zapatillas_a = datos.id_zapatillas_a
                id_zapatillas_n = datos.id_zapatillas_n
                talla = datos.talla
                precio_venta = datos.precio_venta
                fecha_venta = datos.fecha_venta
                
            else:
                mensaje = "La venta no existe"
    return render(request, "ConsultarVenta.html",{"mensaje":mensaje, "id_zapatillas_a": id_zapatillas_a, "id_zapatillas_n":id_zapatillas_n,  "talla":talla,"precio_venta":precio_venta, "fecha_venta":fecha_venta})

def crearUsuario(request):
    mensaje = ""
    if request.method == "POST":
        nombre = request.POST['nombre']
        cedula = request.POST['cedula']
        apellidos = request.POST['apellidos']
        direccion = request.POST['direccion']
        telefono = request.POST['telefono']
        email = request.POST['correo']
        tipo_usuario = request.POST['tipo_usuario']
        contrasena = request.POST['contrasena']
        estado = request.POST['estado']

        if len(nombre) !=0:
            u = Usuario(nombre = nombre, cedula=cedula,apellidos=apellidos, direccion=direccion, telefono = telefono, correo=email, tipo_usuario=tipo_usuario, contrasena=contrasena, estado= estado)    
            u.save()
            mensaje = "guardado exitosamente"
    return render(request, "CrearUsuario.html", {"mensaje":mensaje})

def modificarUsuario(request):
    boton = ""
    mensaje = ""
    nombre= ""
    cedula = ""
    direccion= ""
    apellido1 =""
    rol = ""
    correo = ""
    estado=""
    if request.method == "POST" and request.POST['boton'] == "Buscar usuario a modificar":
        email = request.POST['emailUser']
        if len(email) !=0:            
            u = Usuario.objects.filter(correo=email)   
            if len(u) == 1:
                datos = u.get()
                nombre = datos.nombre
                apellido1 = datos.apellidos
                cedula = datos.cedula
                direccion = datos.direccion
                rol = datos.tipo_usuario
                correo = datos.correo
                contrasena= datos.contrasena
                estado = datos.estado
                boton = "Confirmar Modificación"
                return render(request, "ModificarUsuario.html", {"boton":boton, "nombre": nombre, "estadoEmail": 'readonly', "apellido1": apellido1, "cedula":cedula, "direccion":direccion,"rol":rol, "correo": correo, "contrasena": contrasena,"estado":estado})
            if len(u) != 1:
                mensaje = "No se encontró el usuario"
                boton = "Buscar usuario a modificar"
                rol="-Seleccione Rol-"
                return render(request, "ModificarUsuario.html", {"boton":boton, "nombre": nombre, "estadoEmail": 'readonly', "apellido1": apellido1, "cedula":cedula, "direccion":direccion,"rol":rol, "correo": correo, "contrasena": contrasena,"estado":estado})
        else:
            mensaje = "No se encontró el usuario"
            boton = "Buscar usuario a modificar"
            rol="-Seleccione Rol-"
            return render(request, "ModificarUsuario.html", {"mensaje":mensaje, "boton": boton, "rol":rol, "estadoEmail": 'required'})

    if request.method == "POST" and request.POST['boton'] == "Confirmar Modificación":
        email2 = request.POST['emailUser']
        if len(request.POST['Nombre'])>0 and len(request.POST['PrimerApellido'])>0 and len(request.POST['SegundoApellido'])>0 and len(request.POST['direccion'])>0 and len(request.POST['Contraseña'])>0:
            u = Usuario.objects.get(correo=email2)   
            u.nombre = request.POST['Nombre']
            u.apellidos = request.POST['PrimerApellido']
            u.cedula = request.POST['SegundoApellido']
            u.direccion = request.POST['direccion']
            u.estado = request.POST['estado']
            u.tipo_usuario = request.POST['rolUser']
            
            if len(request.POST['rolUser']) != 0:
                u.tipo_usuario = request.POST['rolUser']
            u.save()
            mensaje = "Se modificó exitosamente"
            boton = "Buscar usuario a modificar"
            estado="--Seleccione Estado--"
            rol="-Seleccione Rol-"
            return render(request, "ModificarUsuario.html", {"mensaje":mensaje, "boton": boton, "estado":estado,"rol":rol, "estadoEmail": 'required'})        
    else:
        boton = "Buscar usuario a modificar"
        rol="--Seleccione Rol--"
        estado="--Seleccione Estado--"
        return render(request, "ModificarUsuario.html", {"boton":boton,"rol":rol,"estado":estado, "estadoEmail": 'required'})

def modificarVenta(request):
    boton = ""
    mensaje = ""
    zapatillas_a_alm = ""
    zapatillas_n_alm = ""
    talla = ""
    precio_venta = ""
    fecha_venta = ""
    if request.method == "POST" and request.POST['boton'] == "Buscar venta a modificar":
        fecha_venta = request.POST['fecha_venta']
        if len(fecha_venta) !=0:            
            u = Ventas_almacen.objects.filter(fecha_venta=fecha_venta)   
            if len(u) == 1:
                datos = u.get()
                zapatillas_a_alm = datos.id_zapatillas_a
                zapatillas_n_alm = datos.id_zapatillas_n
                talla = datos.talla
                precio_venta = datos.precio_venta
                fecha_venta = datos.fecha_venta
                
                boton = "Confirmar Modificación"
                return render(request, "ModificarVenta.html", {"boton":boton, "zapatillas_a_alm": zapatillas_a_alm,"zapatillas_n_alm":zapatillas_n_alm,"talla":talla, "precio_venta":precio_venta,"fecha_venta": 'readonly'})
            if len(u) != 1:
                mensaje = "No se encontró"
                boton = "Buscar venta a modificar"
                return render(request, "ModificarVenta.html", {"boton":boton, "zapatillas_a_alm": zapatillas_a_alm,"zapatillas_n_alm":zapatillas_n_alm,"talla":talla, "precio_venta":precio_venta,"fecha_venta": fecha_venta})
        else:
            mensaje = "No se encontró el usuario"
            boton = "Buscar venta a modificar"
            return render(request, "ModificarVenta.html", {"boton":boton, "zapatillas_a_alm": zapatillas_a_alm,"zapatillas_n_alm":zapatillas_n_alm,"talla":talla, "precio_venta":precio_venta,"fecha_venta": fecha_venta})

    if request.method == "POST" and request.POST['boton'] == "Confirmar Modificación":
        fecha2 = request.POST['fecha_venta']
        if len(request.POST['id_zapatillas_a'])>0 and len(request.POST['id_zapatillas_n'])>0 and len(request.POST['talla'])>0 and len(request.POST['precio_venta'])>0 and len(request.POST['fecha_venta'])>0:
            u = Ventas_almacen.objects.get(fecha_venta=fecha2)   
            u.zapatillas_a_alm = request.POST['id_zapatillas_a']
            u.zapatillas_n_alm = request.POST['id_zapatillas_n']
            u.talla = request.POST['talla']
            u.precio_venta = request.POST['precio_venta']
            u.fecha_venta = request.POST['fecha_venta']
            
            if len(request.POST['rolUser']) != 0:
                u.tipo_usuario = request.POST['rolUser']
            u.save()
            mensaje = "Se modificó exitosamente"
            boton = "Buscar venta a modificar"
            return render(request, "ModificarVenta.html", {"mensaje":mensaje, "boton": boton, "fecha_venta": 'required'})        
    else:
        boton = "Buscar venta a modificar"
        return render(request, "ModificarVenta.html", {"boton":boton,"fecha_venta": fecha_venta})

def modificarVentaEL(request):
    boton = ""
    mensaje = ""
    zapatillas_a_alm = ""
    zapatillas_n_alm = ""
    talla = ""
    precio_venta = ""
    fecha_venta = ""
    if request.method == "POST" and request.POST['boton'] == "Buscar venta a modificar":
        fecha_venta = request.POST['fecha_venta']
        if len(fecha_venta) !=0:            
            u = Ventas_linea.objects.filter(fecha_venta=fecha_venta)   
            if len(u) == 1:
                datos = u.get()
                zapatillas_a_alm = datos.id_zapatillas_a
                zapatillas_n_alm = datos.id_zapatillas_n
                talla = datos.talla
                precio_venta = datos.precio_venta
                fecha_venta = datos.fecha_venta
                
                boton = "Confirmar Modificación"
                return render(request, "ModificarVentaEL.html", {"boton":boton, "zapatillas_a_alm": zapatillas_a_alm,"zapatillas_n_alm":zapatillas_n_alm,"talla":talla, "precio_venta":precio_venta,"fecha_venta": 'readonly'})
            if len(u) != 1:
                mensaje = "No se encontró"
                boton = "Buscar venta a modificar"
                return render(request, "ModificarVentaEL.html", {"boton":boton, "zapatillas_a_alm": zapatillas_a_alm,"zapatillas_n_alm":zapatillas_n_alm,"talla":talla, "precio_venta":precio_venta,"fecha_venta": fecha_venta})
        else:
            mensaje = "No se encontró el usuario"
            boton = "Buscar venta a modificar"
            return render(request, "ModificarVentaEL.html", {"boton":boton, "zapatillas_a_alm": zapatillas_a_alm,"zapatillas_n_alm":zapatillas_n_alm,"talla":talla, "precio_venta":precio_venta,"fecha_venta": fecha_venta})

    if request.method == "POST" and request.POST['boton'] == "Confirmar Modificación":
        fecha2 = request.POST['fecha_venta']
        if len(request.POST['id_zapatillas_a'])>0 and len(request.POST['id_zapatillas_n'])>0 and len(request.POST['talla'])>0 and len(request.POST['precio_venta'])>0 and len(request.POST['fecha_venta'])>0:
            u = Ventas_linea.objects.get(fecha_venta=fecha2)   
            u.zapatillas_a_alm = request.POST['id_zapatillas_a']
            u.zapatillas_n_alm = request.POST['id_zapatillas_n']
            u.talla = request.POST['talla']
            u.precio_venta = request.POST['precio_venta']
            u.fecha_venta = request.POST['fecha_venta']
            
            if len(request.POST['rolUser']) != 0:
                u.tipo_usuario = request.POST['rolUser']
            u.save()
            mensaje = "Se modificó exitosamente"
            boton = "Buscar venta a modificar"
            return render(request, "ModificarVentaEL.html", {"mensaje":mensaje, "boton": boton, "fecha_venta": 'required'})        
    else:
        boton = "Buscar venta a modificar"
        return render(request, "ModificarVentaEL.html", {"boton":boton,"fecha_venta": fecha_venta})

def eliminarUsuario(request):
    boton = ""
    mensaje = ""
    nombre= ""
    cedula = ""
    apellido1 =""
    rol = ""
    correo = ""
    if request.method == "POST" and request.POST['boton'] == "Buscar usuario a eliminar":
        email = request.POST['emailUser']
        if len(email) !=0:            
            u = Usuario.objects.filter(correo=email)   
            if len(u) == 1:
                datos = u.get()
                nombre = datos.nombre
                apellido1 = datos.apellidos
                cedula = datos.cedula
                rol = datos.tipo_usuario
                correo = datos.correo
                contrasena= datos.contrasena
                boton = "Confirmar Eliminación"
                return render(request, "EliminarUsuario.html", {"boton":boton, "nombre": nombre,  "apellido":apellido1,"cedula":cedula, "rol":rol, "correo": correo, "contrasena": contrasena})
            if len(u) != 1:
                mensaje = "No se encontró el usuario"
                boton = "Buscar usuario a eliminar"
                return render(request, "EliminarUsuario.html", {"mensaje":mensaje, "boton": boton})
        else:
            mensaje = "No se encontró el usuario"
            boton = "Buscar usuario a eliminar"
            return render(request, "EliminarUsuario.html", {"mensaje":mensaje, "boton": boton})
    
    if request.method == "POST" and request.POST['boton'] == "Confirmar Eliminación":
        email2 = request.POST['emailUser']
        if len(request.POST['emailUser'])>0 :
            u = Usuario.objects.get(correo=email2)   
            u.delete()
            mensaje = "Se eliminó exitosamente"
            boton = "Buscar usuario a eliminar"
            return render(request, "EliminarUsuario.html", {"mensaje":mensaje, "boton": boton})        
    else:
        boton = "Buscar usuario a eliminar"
        return render(request, "EliminarUsuario.html", {"boton":boton})

def interfazAdmin(request):
    return render(request, "InterfazAdmin.html")

def interfazEmpleado(request):
    return render(request, "InterfazEmpleado.html")

def consultarUsuario(request):
    mensaje = ""
    nombre= ""
    apellido1 =""
    cedula = ""
    rol = ""
    direccion = ""
    telefono = ""
    correo = ""
    estado = ""
    if request.method == "POST":
        email = request.POST['emailUser']
        if len(email) !=0:            
            u = Usuario.objects.filter(correo=email)   
            if len(u) == 1:
                datos = u.get()
                nombre = datos.nombre
                apellido1 = datos.apellidos
                cedula = datos.cedula
                rol = datos.tipo_usuario
                direccion = datos.direccion
                telefono = datos.telefono
                correo = datos.correo
                estado =datos.estado
            else:
                mensaje = "El usuario no existe"
    return render(request, "ConsultarUsuario.html",{"mensaje":mensaje, "nombre": nombre, "apellido1": apellido1, "cedula":cedula, "rol":rol, "direccion":direccion, "telefono":telefono, "correo": correo, "estado":estado})
    
def consultarGastoVA(request):
    mensaje = ""
    costo= ""
    fecha =""
    descripcion = ""
    
    if request.method == "POST":
        fecha = request.POST['fecha']
        if len(fecha) !=0:            
            u = GastosVariable_Almacen.objects.filter(fecha=fecha)   
            if len(u) == 1:
                datos = u.get()
                costo = datos.costo
                fecha = datos.fecha
                descripcion = datos.descripcion
                
            else:
                mensaje = "El gasto no existe"
    return render(request, "ConsultarGastoVA.html",{"mensaje":mensaje, "costo": costo, "fecha": fecha, "descripcion":descripcion})

def consultarGastoVL(request):
    mensaje = ""
    costo= ""
    fecha =""
    descripcion = ""
    
    if request.method == "POST":
        fecha = request.POST['fecha']
        if len(fecha) !=0:            
            u = GastosVariable_Linea.objects.filter(fecha=fecha)   
            if len(u) == 1:
                datos = u.get()
                costo = datos.costo
                fecha = datos.fecha
                descripcion = datos.descripcion
                
            else:
                mensaje = "El gasto no existe"
    return render(request, "ConsultarGastoVL.html",{"mensaje":mensaje, "costo": costo, "fecha": fecha, "descripcion":descripcion})

def consultarClientes(request):
    return render(request, "ConsultarClientes.html")

def  avancesDeObras(request):
    return render(request, "AvancesDeObras.html")

def crearZapatillaAF(request):
    mensaje = ""
    if request.method == "POST":
        estilo = request.POST['estilo']
        precio_compra = request.POST['precio_compra']
        proveedor = request.POST['proveedor']
        t43 = request.POST['43']
        t42 = request.POST['42']
        t41 = request.POST['41']
        t40 = request.POST['40']
        t39 = request.POST['39']
        t38 = request.POST['38']
        t37 = request.POST['37']
        t36 = request.POST['36']
        t35 = request.POST['35']
        t34 = request.POST['34']
        t33 = request.POST['33']

        if len(estilo) !=0:
            z = Zapatilla_a_almacen(estilo = estilo, precio_compra=precio_compra,proveedor=proveedor, talla_43=t43, talla_42=t42, talla_41=t41, talla_40=t40,talla_39=t39,talla_38=t38,talla_37=t37,talla_36=t36,talla_35=t35,talla_34=t34,talla_33=t33)    
            z.save()
            mensaje = "guardado exitosamente"
    return render(request, "CrearZapatillaAF.html", {"mensaje":mensaje})
def crearZapatillaNF(request):
    mensaje = ""
    if request.method == "POST":
        estilo = request.POST['estilo_n_f']
        precio_compra = request.POST['precio_compra_n_f']
        proveedor = request.POST['proveedor_n_f']
        t32 = request.POST['32']
        t31 = request.POST['31']
        t30 = request.POST['30']
        t29 = request.POST['29']
        t28 = request.POST['28']
        t27 = request.POST['27']
        t26 = request.POST['26']
        t25 = request.POST['25']
        t24 = request.POST['24']
        t23 = request.POST['23']
        t22 = request.POST['22']

        if len(estilo) !=0:
            zna = Zapatilla_n_almacen(estilo = estilo, precio_compra=precio_compra,proveedor=proveedor, talla_32=t32, talla_31=t31, talla_30=t30,talla_29=t29,talla_28=t28,talla_27=t27,talla_26=t26,talla_25=t25,talla_24=t24,talla_23=t23,talla_22=t22)    
            zna.save()
            mensaje = "guardado exitosamente"
    return render(request, "CrearZapatillaNF.html", {"mensaje":mensaje})    
def crearZapatillaAL(request):
    mensaje = ""
    if request.method == "POST":
        estilo = request.POST['estilo_a_l']
        precio_compra = request.POST['precio_compra_a_l']
        proveedor = request.POST['proveedor_a_l']
        t43 = request.POST['43_l']
        t42 = request.POST['42_l']
        t41 = request.POST['41_l']
        t40 = request.POST['40_l']
        t39 = request.POST['39_l']
        t38 = request.POST['38_l']
        t37 = request.POST['37_l']
        t36 = request.POST['36_l']
        t35 = request.POST['35_l']
        t34 = request.POST['34_l']
        t33 = request.POST['33_l']

        if len(estilo) !=0:
            zal = Zapatilla_a_linea(estilo = estilo, precio_compra=precio_compra,proveedor=proveedor, talla_43=t43, talla_42=t42, talla_41=t41, talla_40=t40,talla_39=t39,talla_38=t38,talla_37=t37,talla_36=t36,talla_35=t35,talla_34=t34,talla_33=t33)    
            zal.save()
            mensaje = "guardado exitosamente"
    return render(request, "CrearZapatillaAL.html", {"mensaje":mensaje})
def crearZapatillaNL(request):
    mensaje = ""
    if request.method == "POST":
        estilo = request.POST['estilo_n_l']
        precio_compra = request.POST['precio_compra_n_l']
        proveedor = request.POST['proveedor_n_l']
        t32 = request.POST['32_l']
        t31 = request.POST['31_l']
        t30 = request.POST['30_l']
        t29 = request.POST['29_l']
        t28 = request.POST['28_l']
        t27 = request.POST['27_l']
        t26 = request.POST['26_l']
        t25 = request.POST['25_l']
        t24 = request.POST['24_l']
        t23 = request.POST['23_l']
        t22 = request.POST['22_l']

        if len(estilo) !=0:
            znl = Zapatilla_n_linea(estilo = estilo, precio_compra=precio_compra,proveedor=proveedor, talla_32=t32, talla_31=t31, talla_30=t30,talla_29=t29,talla_28=t28,talla_27=t27,talla_26=t26,talla_25=t25,talla_24=t24,talla_23=t23,talla_22=t22)    
            znl.save()
            mensaje = "guardado exitosamente"
    return render(request, "CrearZapatillaNL.html", {"mensaje":mensaje})
def registrarPedidoAF(request):
    mensaje = ""
    if request.method == "POST":
        estilo = request.POST['estilo_p_p_a']
        t43 = request.POST['43_p_p_a']
        t42 = request.POST['42_p_p_a']
        t41 = request.POST['41_p_p_a']
        t40 = request.POST['40_p_p_a']
        t39 = request.POST['39_p_p_a']
        t38 = request.POST['38_p_p_a']
        t37 = request.POST['37_p_p_a']
        t36 = request.POST['36_p_p_a']
        t35 = request.POST['35_p_p_a']
        t34 = request.POST['34_p_p_a']
        t33 = request.POST['33_p_p_a']

        if len(estilo) !=0:           
            estiloP = Zapatilla_a_almacen.objects.filter(estilo=estilo) 
            if len(estiloP) == 1:
                datos = estiloP.get()
                u = Zapatilla_a_almacen.objects.get(estilo=estilo)  
                u.talla_43 = int(t43)+datos.talla_43
                u.talla_42 = int(t42)+datos.talla_42
                u.talla_41 = int(t41)+datos.talla_41
                u.talla_40 = int(t40)+datos.talla_40
                u.talla_39 = int(t39)+datos.talla_39
                u.talla_38 = int(t38)+datos.talla_38
                u.talla_37 = int(t37)+datos.talla_37
                u.talla_36 = int(t36)+datos.talla_36
                u.talla_35 = int(t35)+datos.talla_35
                u.talla_34 = int(t34)+datos.talla_34
                u.talla_33 = int(t33)+datos.talla_33
                mensaje = "guardado exitosamente"
                u.save()
    return render(request, "RegistrarPedidoAF.html", {"mensaje":mensaje}) 
def registrarPedidoNF(request):
    mensaje = ""
    if request.method == "POST":
        estilo = request.POST['estilo_p_p_n']
        t32 = request.POST['32_p_p_n']
        t31 = request.POST['31_p_p_n']
        t30 = request.POST['30_p_p_n']
        t29 = request.POST['29_p_p_n']
        t28 = request.POST['28_p_p_n']
        t27 = request.POST['27_p_p_n']
        t26 = request.POST['26_p_p_n']
        t25 = request.POST['25_p_p_n']
        t24 = request.POST['24_p_p_n']
        t23 = request.POST['23_p_p_n']
        t22 = request.POST['23_p_p_n']

        if len(estilo) !=0:           
            estiloP = Zapatilla_n_almacen.objects.filter(estilo=estilo) 
            if len(estiloP) == 1:
                datos = estiloP.get()
                u = Zapatilla_n_almacen.objects.get(estilo=estilo) 
                u.talla_32 = int(t32)+datos.talla_32
                u.talla_31 = int(t31)+datos.talla_31
                u.talla_30 = int(t30)+datos.talla_30
                u.talla_29 = int(t29)+datos.talla_29
                u.talla_28 = int(t28)+datos.talla_28
                u.talla_27 = int(t27)+datos.talla_27
                u.talla_26 = int(t26)+datos.talla_26
                u.talla_25 = int(t25)+datos.talla_25
                u.talla_24 = int(t24)+datos.talla_24
                u.talla_23 = int(t23)+datos.talla_23
                u.talla_22 = int(t22)+datos.talla_22
                mensaje = "guardado exitosamente"
                u.save()
    return render(request, "RegistrarPedidoNF.html", {"mensaje":mensaje})     
def registrarPedidoAL(request):
    mensaje = ""
    if request.method == "POST":
        estilo = request.POST['estilo_p_l_a']
        t43 = request.POST['43_p_l_a']
        t42 = request.POST['42_p_l_a']
        t41 = request.POST['41_p_l_a']
        t40 = request.POST['40_p_l_a']
        t39 = request.POST['39_p_l_a']
        t38 = request.POST['38_p_l_a']
        t37 = request.POST['37_p_l_a']
        t36 = request.POST['36_p_l_a']
        t35 = request.POST['35_p_l_a']
        t34 = request.POST['34_p_l_a']
        t33 = request.POST['33_p_l_a']

        if len(estilo) !=0:           
            estiloP = Zapatilla_a_linea.objects.filter(estilo=estilo) 
            if len(estiloP) == 1:
                datos = estiloP.get()
                u = Zapatilla_a_linea.objects.get(estilo=estilo)  
                u.talla_43 = int(t43)+datos.talla_43
                u.talla_42 = int(t42)+datos.talla_42
                u.talla_41 = int(t41)+datos.talla_41
                u.talla_40 = int(t40)+datos.talla_40
                u.talla_39 = int(t39)+datos.talla_39
                u.talla_38 = int(t38)+datos.talla_38
                u.talla_37 = int(t37)+datos.talla_37
                u.talla_36 = int(t36)+datos.talla_36
                u.talla_35 = int(t35)+datos.talla_35
                u.talla_34 = int(t34)+datos.talla_34
                u.talla_33 = int(t33)+datos.talla_33
                mensaje = "guardado exitosamente"
                u.save()
    return render(request, "RegistrarPedidoAL.html", {"mensaje":mensaje}) 
def registrarPedidoNL(request):
    mensaje = ""
    if request.method == "POST":
        estilo = request.POST['estilo_p_l_n']
        t32 = request.POST['32_p_l_n']
        t31 = request.POST['31_p_l_n']
        t30 = request.POST['30_p_l_n']
        t29 = request.POST['29_p_l_n']
        t28 = request.POST['28_p_l_n']
        t27 = request.POST['27_p_l_n']
        t26 = request.POST['26_p_l_n']
        t25 = request.POST['25_p_l_n']
        t24 = request.POST['24_p_l_n']
        t23 = request.POST['23_p_l_n']
        t22 = request.POST['23_p_l_n']

        if len(estilo) !=0:           
            estiloP = Zapatilla_n_linea.objects.filter(estilo=estilo) 
            if len(estiloP) == 1:
                datos = estiloP.get()
                u = Zapatilla_n_linea.objects.get(estilo=estilo) 
                u.talla_32 = int(t32)+datos.talla_32
                u.talla_31 = int(t31)+datos.talla_31
                u.talla_30 = int(t30)+datos.talla_30
                u.talla_29 = int(t29)+datos.talla_29
                u.talla_28 = int(t28)+datos.talla_28
                u.talla_27 = int(t27)+datos.talla_27
                u.talla_26 = int(t26)+datos.talla_26
                u.talla_25 = int(t25)+datos.talla_25
                u.talla_24 = int(t24)+datos.talla_24
                u.talla_23 = int(t23)+datos.talla_23
                u.talla_22 = int(t22)+datos.talla_22
                mensaje = "guardado exitosamente"
                u.save()
    return render(request, "RegistrarPedidoNL.html", {"mensaje":mensaje})
def ingresarGastosVariablesF(request):
    mensaje = ""
    if request.method == "POST":
        Costo = request.POST['costoG_v_f']
        Descripcion = request.POST['descripcionG_v_f']

        if len(Costo) !=0:
            gvf = Gastos_Variable_almacen(costo = Costo, fecha = datetime.today().strftime('%Y-%m-%d'), descripcion = Descripcion)
            gvf.save()
            mensaje = "guardado exitosamente"
    return render(request, "ingresarGastosVariablesF.html", {"mensaje":mensaje})
def ingresarGastosFijosF(request):
    mensaje = ""
    if request.method == "POST":
        Costo = request.POST['costoG_f_f']
        Descripcion = request.POST['descripcionG_f_f']

        if len(Costo) !=0:
            gff = Gastos_Fijos_Almacen(costo = Costo, fecha = datetime.today().strftime('%Y-%m-%d'), descripcion = Descripcion)
            gff.save()
            mensaje = "guardado exitosamente"
    return render(request, "ingresarGastosFijosF.html", {"mensaje":mensaje})
def ingresarGastosVariablesL(request):
    mensaje = ""
    if request.method == "POST":
        Costo = request.POST['costoG_v_l']
        Descripcion = request.POST['descripcionG_v_l']

        if len(Costo) !=0:
            gvl = Gastos_Variable_linea(costo = Costo, fecha = datetime.today().strftime('%Y-%m-%d'), descripcion = Descripcion)
            gvl.save()
            mensaje = "guardado exitosamente"
    return render(request, "ingresarGastosVariablesL.html", {"mensaje":mensaje})  
def listarVenta(request):
    ventas = Ventas_almacen.objects.all()
    contexto = {"ventas":ventas}
    return render(request, "ConsultarVenta.html", contexto)
    
def listarVentaEL(request):
    ventas = Ventas_linea.objects.all()
    contexto = {"ventas":ventas}
    return render(request, "ConsultarVentaEL.html", contexto)

def listarUsuarios(request):
    usuarios = Usuario.objects.all()
    contexto = {"usuarios":usuarios}
    return render(request, "VerUsuarios.html", contexto)
def verGastosFijos(request):
    gastos = Gastos_Fijos_Almacen.objects.all()
    contexto = {"gastos": gastos}
    return render(request, "VerGastosFijos.html", contexto)
def verInventarioAF(request):
    inventario = Zapatilla_a_almacen.objects.all()
    contexto = {"inventario": inventario}
    return render(request, "VerInventarioAF.html", contexto)
def verInventarioNF(request):
    inventario = Zapatilla_n_almacen.objects.all()
    contexto = {"inventario": inventario}
    return render(request, "VerInventarioNF.html", contexto)
def verInventarioAL(request):
    inventario = Zapatilla_a_linea.objects.all()
    contexto = {"inventario": inventario}
    return render(request, "VerInventarioAL.html", contexto)
def verInventarioNL(request):
    inventario = Zapatilla_n_linea.objects.all()
    contexto = {"inventario": inventario}
    return render(request, "VerInventarioNL.html", contexto)
def ModificarGastosFijos(request):
    boton = ""
    mensaje = ""
    id_= ""
    descripcion = ""
    costo= ""
    if request.method == "POST" and request.POST['boton_'] == "Buscar gasto a modificar":
        id_ = request.POST['id']
        if len(id_) !=0:            
            u = Gastos_Fijos_Almacen.objects.filter(id_gasto_variable_l=id_)   
            if len(u) == 1:
                datos = u.get()
                descripcion = datos.descripcion
                costo = datos.costo
                boton = "Confirmar Modificación"
                return render(request, "ModificarGastosFijosF.html", {"boton_":boton, "descripcion":descripcion,"costo":costo,"id":id_,"estadoId": 'readonly'})
            if len(u) != 1:
                mensaje = "No se encontró el gasto"
                boton = "Buscar gasto a modificar"
                return render(request, "ModificarGastosFijosF.html", {"boton_":boton,"descripcion":descripcion,"costo":costo,"estadoId": 'readonly' })
        else:
            mensaje = "No se encontró el usuario"
            boton = "Buscar gasto a modificar"
            return render(request, "ModificarGastosFijosF.html", {"boton_":boton,"descripcion":descripcion,"costo":costo,"estadoId": 'required' })

    if request.method == "POST" and request.POST['boton_'] == "Confirmar Modificación":
        id_ = request.POST['id']
        if len(request.POST['Descripcion'])>0 and len(request.POST['Costo'])>0:
            u = Gastos_Fijos_Almacen.objects.get(id_gasto_variable_l=id_)   
            u.descripcion = request.POST['Descripcion']
            u.costo = request.POST['Costo']
            u.save()
            mensaje = "Se modificó exitosamente"
            boton = "Buscar gasto a modificar"
            return render(request, "ModificarGastosFijosF.html", {"mensaje":mensaje,"boton_":boton,"descripcion":descripcion,"costo":costo,"estadoId": 'required' })       
    else:
        boton = "Buscar gasto a modificar"
        return render(request, "ModificarGastosFijosF.html", {"boton_":boton, "estadoId": 'required'})

def ConsultarZapatillaAF(request):  
    mensaje = ""
    t43 = ""
    t42 = ""
    t41 = ""
    t40 = ""
    t39 = ""
    t38 = ""
    t37 = ""
    t36 = ""
    t35 = ""
    t34 = ""
    t33 = ""
    if request.method == "POST":
        estilo = request.POST['estiloZapatillaAF']
        if len(estilo) !=0:            
            u = Zapatilla_a_almacen.objects.filter(estilo=estilo)   
            if len(u) == 1:
                datos = u.get()
                t43 = datos.talla_43
                t42 = datos.talla_42
                t41 = datos.talla_41
                t40 = datos.talla_40
                t39 = datos.talla_39
                t38 = datos.talla_38
                t37 = datos.talla_37
                t36 = datos.talla_36
                t35 = datos.talla_35
                t34 = datos.talla_34
                t33 = datos.talla_33
            else:
                mensaje = "La zapatilla no existe"
    return render(request, "ConsultarZapatillaAF.html",  {"mensaje":mensaje, "t43":t43,"t42":t42,"t41":t41,"t40":t40,"t39":t39,"t38":t38,"t37":t37,"t36":t36,"t35":t35,"t34":t34,"t33":t33})
def ConsultarZapatillaNF(request):  
    mensaje = ""
    t32 = ""
    t31 = ""
    t30 = ""
    t29 = ""
    t28 = ""
    t27 = ""
    t26 = ""
    t25 = ""
    t24 = ""
    t23 = ""
    t22 = ""
    if request.method == "POST":
        estilo = request.POST['estiloZapatillaNF']
        if len(estilo) !=0:            
            u = Zapatilla_n_almacen.objects.filter(estilo=estilo)   
            if len(u) == 1:
                datos = u.get()
                t32 = datos.talla_32
                t31 = datos.talla_31
                t30 = datos.talla_30
                t29 = datos.talla_29
                t28 = datos.talla_28
                t27 = datos.talla_27
                t26 = datos.talla_26
                t25 = datos.talla_25
                t24 = datos.talla_24
                t23 = datos.talla_23
                t22 = datos.talla_22
            else:
                mensaje = "La zapatilla no existe"
    return render(request, "ConsultarZapatillaNF.html",  {"mensaje":mensaje,"t32":t32,"t31":t31,"t30":t30,"t29":t29,"t28":t28,"t27":t27,"t26":t26,"t25":t25,"t24":t24,"t23":t23,"t22":t22})
def ConsultarZapatillaAL(request):  
    mensaje = ""
    t43 = ""
    t42 = ""
    t41 = ""
    t40 = ""
    t39 = ""
    t38 = ""
    t37 = ""
    t36 = ""
    t35 = ""
    t34 = ""
    t33 = ""
    if request.method == "POST":
        estilo = request.POST['estiloZapatillaAL']
        if len(estilo) !=0:            
            u = Zapatilla_a_linea.objects.filter(estilo=estilo)   
            if len(u) == 1:
                datos = u.get()
                t43 = datos.talla_43
                t42 = datos.talla_42
                t41 = datos.talla_41
                t40 = datos.talla_40
                t39 = datos.talla_39
                t38 = datos.talla_38
                t37 = datos.talla_37
                t36 = datos.talla_36
                t35 = datos.talla_35
                t34 = datos.talla_34
                t33 = datos.talla_33
            else:
                mensaje = "La zapatilla no existe"
    return render(request, "ConsultarZapatillaAL.html",  {"mensaje":mensaje, "t43_":t43,"t42_":t42,"t41_":t41,"t40_":t40,"t39_":t39,"t38_":t38,"t37_":t37,"t36_":t36,"t35_":t35,"t34_":t34,"t33_":t33})
def ConsultarZapatillaNL(request):  
    mensaje = ""
    t32 = ""
    t31 = ""
    t30 = ""
    t29 = ""
    t28 = ""
    t27 = ""
    t26 = ""
    t25 = ""
    t24 = ""
    t23 = ""
    t22 = ""
    if request.method == "POST":
        estilo = request.POST['estiloZapatillaNL']
        if len(estilo) !=0:            
            u = Zapatilla_n_linea.objects.filter(estilo=estilo)   
            if len(u) == 1:
                datos = u.get()
                t32 = datos.talla_32
                t31 = datos.talla_31
                t30 = datos.talla_30
                t29 = datos.talla_29
                t28 = datos.talla_28
                t27 = datos.talla_27
                t26 = datos.talla_26
                t25 = datos.talla_25
                t24 = datos.talla_24
                t23 = datos.talla_23
                t22 = datos.talla_22
            else:
                mensaje = "La zapatilla no existe"
    return render(request, "ConsultarZapatillaNL.html",  {"mensaje":mensaje,"t32_":t32,"t31_":t31,"t30_":t30,"t29_":t29,"t28_":t28,"t27_":t27,"t26_":t26,"t25_":t25,"t24_":t24,"t23_":t23,"t22_":t22})

def listarVentaPorMesF(request):
    ventas = Ventas_almacen.objects.filter(fecha_venta__range=["2020-12-01", "2022-12-31"])
    contexto = {"ventas":ventas}
    return render(request, "ConsultarVentasPorMesF.html",contexto)

def registrarMateriales(request):
    mensaje = ""
    print("hola")
    if request.method == "POST":
        proveedor = request.POST['idProveedor']
        nombreItem = request.POST['nombreItem']
        cantidadItem = request.POST['cantidadItem']
        referenciaItem = request.POST['referenciaItem']
        estadoItem = request.POST['estadoItem']
        if len(nombreItem) != 0:
            i = Inventario(proveedor_ID_item = proveedor,nombre_item = nombreItem, cantidad_item=cantidadItem,referencia_item=referenciaItem, estado_item=estadoItem)    
            i.save()
            mensaje = "guardado exitosamente"
    return render(request, "registroMateriales.html", {"mensaje":mensaje})
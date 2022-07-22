from django.db.models.query import EmptyQuerySet
from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render



# Conexión a la base de datos 
from . import models
Usuario = models.Usuario
Ventas_almacen = models.Ventas_almacen


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

    if password == password_db:
        if rol_db == "Admin":
            return render(request, "InterfazAdmin.html")

        if rol_db == "Empleado":
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
        zapatillas_a_alm = request.POST['id_zapatillas_a']
        zapatillas_n_alm = request.POST['id_zapatillas_n']
        talla = request.POST['talla']
        precio_venta = request.POST['precio_venta']
        fecha_venta = request.POST['fecha_venta']

        if len(zapatillas_a_alm) !=0:
            u = Ventas_almacen(id_zapatillas_a = zapatillas_a_alm, id_zapatillas_n=zapatillas_n_alm,talla=talla, precio_venta=precio_venta, fecha_venta = fecha_venta)    
            u.save()
            mensaje = "guardado exitosamente"
    return render(request, "CrearVenta.html", {"mensaje":mensaje})

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
                return render(request, "ModificarUsuario.html", {"mensaje":mensaje, "boton": boton,"rol":rol, "estadoEmail": 'required'})
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
            if len(request.POST['rolUser']) != 0:
                u.rol_usuario = request.POST['rolUser']
            u.contrasena_usuario = request.POST['Contraseña']
            u.save()
            mensaje = "Se modificó exitosamente"
            boton = "Buscar usuario a modificar"
            rol="-Seleccione Rol-"
            return render(request, "ModificarUsuario.html", {"mensaje":mensaje, "boton": boton, "rol":rol, "estadoEmail": 'required'})        
    else:
        boton = "Buscar usuario a modificar"
        rol="--Seleccione Rol--"
        return render(request, "ModificarUsuario.html", {"boton":boton,"rol":rol, "estadoEmail": 'required'})

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
    return render(request, "ConsultarUsuario.html",{"mensaje":mensaje, "nombre": nombre, "apellido1": apellido1, "cedula":cedula,  "rol":rol,"direccion":direccion, "telefono":telefono, "correo": correo, "estado":estado})

def consultarClientes(request):
    return render(request, "ConsultarClientes.html")

def  avancesDeObras(request):
    return render(request, "AvancesDeObras.html")

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

    

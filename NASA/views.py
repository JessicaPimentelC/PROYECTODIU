from cgi import print_environ
from cmath import cos, pi
from email.policy import default
from django.db.models.query import EmptyQuerySet
from django.forms import EmailField
from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render



# Conexión a la base de datos 
from . import models
Usuario = models.Usuario
Zapatilla_a_almacen = models.Zapatillas_a_almacen
Zapatilla_n_almacen = models.Zapatillas_n_almacen
Zapatilla_a_linea = models.Zapatillas_a_linea
Zapatilla_n_linea = models.Zapatillas_n_linea
Ventas_almacen = models.Ventas_almacen
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
    return render(request, "ConsultarGastoVA.html",{"mensaje":mensaje, "costo": costo, "fecha": fecha, "descripcion":descripcion})

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

    

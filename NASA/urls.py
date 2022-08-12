"""Proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('index.html', views.index, name='index'),
    path('register.html/', views.registro, name='register'),
    path('registroMateriales.html/', views.registroMateriales, name='registroMateriales'),
    path('registrarProveedores.html/', views.crearProveedores, name='crearProveedores'),
    path('CrearVenta.html/', views.crearVenta, name='CrearVenta'),
    path('ModificarVenta.html/', views.modificarVenta, name='ModificarVenta'),
    path('ModificarVentaEL.html/', views.modificarVentaEL, name='ModificarVentaEL'),
    path('CrearVentaEL.html/', views.crearVentaEL, name='CrearVentaEL'),
    path('ConsultarVenta.html/', views.listarVenta, name='ConsultarVenta'),
    path('ConsultarVentasPorMesF.html/', views.listarVentaPorMesF, name='ConsultarVentasPorMesF'),
    path('ConsultarVentaEL.html/', views.listarVentaEL, name='ConsultarVentaEL'),
    path('ConsultarGastoVA.html/', views.consultarGastoVA, name='ConsultarGastoVA'),
    path('ConsultarGastoVL.html/', views.consultarGastoVL, name='ConsultarGastoVL'),
    path('VerUsuarios.html/', views.listarUsuarios, name='verUsuarios'),
    path('registrarProveedores.html/', views.crearProveedores, name='crearProveedores'),
    path('verInventario.html/', views.verInventario, name='verInventario'),
    path('verProveedores.html/', views.verProveedores, name='verProveedores'),
    path('verSolicitudesMateriales.html/', views.verSolicitudesMateriales, name='verSolicitudesMateriales'),
    path('solicitarMateriales.html/', views.solicitarMateriales, name='solicitarMateriales'),
    path('solicitarMaterialesObra.html/', views.solicitarMaterialesObra, name='solicitarMaterialesObra'),
    path('interfazJefeAlmacen.html/', views.interfazJefeAlmacen, name='interfazJefeAlmacen'),
    path('interfazJefeObra.html/', views.interfazJefeObra, name='interfazJefeObra'),
    path('forgot-password.html/', views.forgotPassword, name='forgot-password'),
    path('404.html/', views.error404, name='404'),
    path('blank.html/', views.blank, name='blank'),
    path('buttons.html/', views.buttons, name='buttons'),
    path('cards.html/', views.cards, name='cards'),
    path('charts.html/', views.charts, name='charts'),
    path('CrearCliente.html/', views.crearCliente, name='CrearCliente'),
    path('SolitudObras.html/', views.solicitudObras, name='SolicitudObras'),
    path('ModificarCliente.html/', views.modificarCliente, name='ModificarCliente'),
    path('EliminarCliente.html/', views.eliminarCliente, name='EliminarCliente'),
    path('ListaCliente.html/', views.listaCliente, name='ListaCliente'),
    path('CrearUsuario.html/', views.crearUsuario, name='CrearUsuario'),
    path('CrearZapatillaAF.html/', views.crearZapatillaAF, name='crearZapatillaAF'),
    path('CrearZapatillaNF.html/', views.crearZapatillaNF, name='crearZapatillaNF'),
    path('CrearZapatillaAL.html/', views.crearZapatillaAL, name='crearZapatillaAL'),
    path('CrearZapatillaNL.html/', views.crearZapatillaNL, name='crearZapatillaNL'),
    path('GestionZapatillas.html/', views.gestionZapatillas, name='GestionZapatillas'),
    path('GestionZapatillasEL.html/', views.gestionZapatillasEL, name='GestionZapatillasEL'),
    path('GestionPedidos.html/', views.gestionPedidos, name='GestionPedidos'),
    path('GestionPedidosEL.html/', views.gestionPedidosEL, name='GestionPedidosEL'),
    path('GestionVentas.html/', views.gestionVentas, name='GestionVentas'),
    path('GestionVentasEL.html/', views.gestionVentasEL, name='GestionVentasEL'),
    path('GestionGastos.html/', views.gestionGastos, name='GestionGastos'),
    path('GestionGastosEL.html/', views.gestionGastosEL, name='GestionGastosEL'),
    path('ingresarGastosVariablesF.html/', views.ingresarGastosVariablesF, name='ingresarGastosVariablesF'),
    path('ingresarGastosFijosF.html/', views.ingresarGastosFijosF, name='ingresarGastosFijosF'),
    path('ingresarGastosVariablesL.html/', views.ingresarGastosVariablesL, name='ingresarGastosVariablesL'),
    path('RegistrarPedidoAF.html/', views.registrarPedidoAF, name='RegistrarPedidoAF'),
    path('RegistrarPedidoNF.html/', views.registrarPedidoNF, name='RegistrarPedidoNF'),
    path('RegistrarPedidoAL.html/', views.registrarPedidoAL, name='RegistrarPedidoAL'),
    path('RegistrarPedidoNL.html/', views.registrarPedidoNL, name='RegistrarPedidoNL'),
    path('registroMateriales.html/', views.registrarMateriales, name='RegistrarMateriales'),
    path('ConsultarUsuario.html/', views.consultarUsuario, name='ConsultarUsuario'),
    path('ConsultarZapatillaAF.html/', views.ConsultarZapatillaAF, name='ConsultarZapatillaAF'),
    path('ConsultarZapatillaAL.html/', views.ConsultarZapatillaAL, name='ConsultarZapatillaAL'),
    path('ConsultarZapatillaNF.html/', views.ConsultarZapatillaNF, name='ConsultarZapatillaNF'),
    path('ConsultarZapatillaNL.html/', views.ConsultarZapatillaNL, name='ConsultarZapatillaNL'),
    path('ModificarUsuario.html/', views.modificarUsuario, name='ModificarUsuario'),
    path('ModificarGastosFijosF.html/', views.ModificarGastosFijos, name='ModificarGastosFijos'),
    path('EliminarUsuario.html/', views.eliminarUsuario, name='EliminarUsuario'),
    path('verUsuario.html/', views.verUsuario, name='VerUsuario'),
    path('VerGastosFijos.html/', views.verGastosFijos, name='verGastosFijos'),
    path('VerInventarioAF.html/', views.verInventarioAF, name='VerInventarioAF'),
    path('VerInventarioAL.html/', views.verInventarioAL, name='VerInventarioAL'),
    path('VerInventarioNF.html/', views.verInventarioNF, name='VerInventarioNF'),
    path('VerInventarioNL.html/', views.verInventarioNL, name='VerInventarioNL'),
    path('InterfazAdmin.html/', views.interfazAdmin, name='InterfazAdmin'),
    path('InterfazEmpleado.html/', views.interfazEmpleado, name='InterfazEmpleado'),
    path('ConsultarClientes.html/', views.consultarClientes, name='ConsultarClientes'),
    path('AvancesDeObras.html/', views.avancesDeObras, name='AvancesDeObras'),
    path('utilities-animation.html/', views.utilitiesAnimation, name='utilities-animation'),
    path('utilities-border.html/', views.utilitiesBorder, name='utilities-border'),
    path('utilities-color.html/', views.utilitiesColor, name='utilities-color'),
    path('utilities-other.htmgil/', views.utilitiesOther, name='utilities-other')
]

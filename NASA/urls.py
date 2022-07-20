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
    path('registroMateriales.html/', views.registrarMateriales, name='RegistrarMateriales'),
    path('ConsultarUsuario.html/', views.consultarUsuario, name='ConsultarUsuario'),
    path('ModificarUsuario.html/', views.modificarUsuario, name='ModificarUsuario'),
    path('EliminarUsuario.html/', views.eliminarUsuario, name='EliminarUsuario'),
    path('InterfazAdmin.html/', views.interfazAdmin, name='InterfazAdmin'),
    path('InterfazEmpleado.html/', views.interfazEmpleado, name='InterfazEmpleado'),
    path('ConsultarClientes.html/', views.consultarClientes, name='ConsultarClientes'),
    path('AvancesDeObras.html/', views.avancesDeObras, name='AvancesDeObras'),
    path('utilities-animation.html/', views.utilitiesAnimation, name='utilities-animation'),
    path('utilities-border.html/', views.utilitiesBorder, name='utilities-border'),
    path('utilities-color.html/', views.utilitiesColor, name='utilities-color'),
    path('utilities-other.html/', views.utilitiesOther, name='utilities-other')
]


import requests
from django.shortcuts import redirect, render

from rest_framework import viewsets
from .models import SolicitudPrestamo
from .serializer import SolicitudPrestamoSerializer
import os

from django.contrib.auth import *
from django.contrib import messages


#La siguiente clase nos permite realizar el crud de los objetos sobre nuestro modelo
class SolicitudPrestamoViewSet(viewsets.ModelViewSet): 
    queryset = SolicitudPrestamo.objects.all()
    serializer_class = SolicitudPrestamoSerializer
    
def solicitudes(request):
    solicitudes= SolicitudPrestamo.objects.all()
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        return render(request, "gestionSolicitudes.html", {"solicitudes": solicitudes})
    else:
        return redirect('/loginPage')


def home(request):
    return render(request, "home.html")

def registrarSolicitud(request):
    if 'txtNombre' in request.POST: 
        nombre = request.POST['txtNombre']     

    if 'txtApellido' in request.POST: 
        apellido = request.POST['txtApellido']     
    
    if 'txtDni' in request.POST: 
        dni=request.POST['txtDni']    
    
    if 'txtMonto' in request.POST: 
        monto = request.POST['txtMonto']     

    if 'gridRadios' in request.POST:
        genero = request.POST['gridRadios']

    if 'txtEmail' in request.POST:
        email = request.POST['txtEmail']

    estaAprobado = validarPrestamo(dni)
    
    solicitud = SolicitudPrestamo.objects.create(nombre=nombre, apellido=apellido, monto=monto,email=email, dni=dni, genero=genero, estaAprobado=estaAprobado)
    return redirect('/')

def validarPrestamo(dni):
    BASE_URL= "https://api.moni.com.ar/api/v4/scoring/pre-score"
    API_KEY =  os.getenv('API_KEY')
    url_request = f"{BASE_URL}/{dni}"
    try:
        response = requests.get(url_request, headers={'credential': API_KEY})
        if response.status_code == requests.status_codes.codes.ok:
            data = response.json()
            if data["has_error"]:
                raise Exception("Hubo un error, intente luego")
            
            if (data['status'] == 'approve'):
                return True
            else:
                return False
    except Exception as e:
        raise e
    
    return response

def eliminarSolicitud(request, dni):
    solicitud = SolicitudPrestamo.objects.get(dni=dni)
    solicitud.delete()
    return redirect('/gestionSolicitudes')

def edicionSolicitud(request, dni):
    solicitud = SolicitudPrestamo.objects.get(dni=dni)
    return render(request, "editarSolicitud.html", {"solicitud": solicitud})

def editarSolicitud(request):

    if 'txtNombre' in request.POST: 
        nombre = request.POST['txtNombre']     

    if 'txtApellido' in request.POST: 
        apellido = request.POST['txtApellido']     
    
    if 'txtMonto' in request.POST: 
        monto = request.POST['txtMonto']     

    if 'gridRadios' in request.POST:
        genero = request.POST['gridRadios']

    if 'txtEmail' in request.POST:
        email = request.POST['txtEmail']

    if 'estaAprobado' in request.POST:
        estaAprobado = request.POST['estaAprobado']
    else:
        estaAprobado=False

    if 'txtDni' in request.POST:
        dni = request.POST['txtDni']
    

    solicitud = SolicitudPrestamo.objects.get(dni=dni)

    solicitud.nombre = nombre
    solicitud.apellido = apellido
    solicitud.genero = genero
    solicitud.monto = monto
    solicitud.email = email
    solicitud.estaAprobado = estaAprobado
    solicitud.save()

    return redirect('/gestionSolicitudes')

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/gestionSolicitudes')
    else:
        return render(request, "login.html")

def loginMio(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/gestionSolicitudes')
    else:
        messages.info(request, 'Username or Password is incorrect')
    context = {}
    return redirect('/gestionSolicitudes')

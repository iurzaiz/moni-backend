
from cmath import e
import os
from django.http import JsonResponse
import requests
from django.shortcuts import redirect, render
from rest_framework import viewsets
from backend.prestamos.permissions import IsPostOrIsAuthenticated

from .models import SolicitudPrestamo
from .serializers import SolicitudPrestamoSerializer
from django.contrib.auth import *
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins, generics
from rest_framework import status

from backend.prestamos import serializers

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

class SolicitudPrestamoApiView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    # API view de Solicitudes prestasmo
    queryset = SolicitudPrestamo.objects.all()
    serializer_class = serializers.SolicitudPrestamoSerializer
    permission_classes = [IsPostOrIsAuthenticated,]

    def get(self, request, *args, **kwargs):
        #Retorna las solicitudes de prestamo
        return self.list(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        request.data._mutable = True
        request.data["estaAprobado"] = validarPrestamo(request.data['dni'])
        request.data._mutable = False
        estaAprobado = validarPrestamo(request.data['dni'])
        solicitud = SolicitudPrestamo.objects.create(nombre=request.data['nombre'], apellido=request.data['apellido'], monto=request.data['monto'],email=request.data['email'], dni=request.data['dni'], genero=request.data['genero'], estaAprobado=estaAprobado)
         
        return Response({'method': 'POST'})


    def put(self, request, id=None):
        #maneja el actualizar un objeto
        solicitud= SolicitudPrestamo.objects.get(id=request.data['id'])
        solicitud.genero = request.data['genero']
        solicitud.monto = request.data['monto']
        solicitud.email = request.data['email']
        solicitud.estaAprobado = request.data['estaAprobado']
        print("se guardo la solicitud")
        solicitud.save()
        return Response({'method': 'PUT'})

    def patch(self, request, pk):
        #maneja actualizacion parcial de un objeto
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        solicitud= SolicitudPrestamo.objects.get(id=request.data['id'])
        solicitud.delete()
        return Response({'method': 'DELETE'})

class SolicitudDetalleApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SolicitudPrestamo.objects.all()
    serializer_class = SolicitudPrestamoSerializer
    permission_class = [IsPostOrIsAuthenticated]


#BORRAR
# El siguiete codigo fue de antes de crear las APIS y front. ORM y django solamente
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

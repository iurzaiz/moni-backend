
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

class SolicitudDetalleApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SolicitudPrestamo.objects.all()
    serializer_class = SolicitudPrestamoSerializer
    permission_class = [IsPostOrIsAuthenticated]

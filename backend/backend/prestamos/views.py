from django.shortcuts import render

from rest_framework import viewsets
from .models import SolicitudPrestamo
from .serializer import SolicitudPrestamoSerializer

#La siguiente clase nos permite realizar el crud de los objetos sobre nuestro modelo
class SolicitudPrestamoViewSet(viewsets.ModelViewSet): 
    queryset = SolicitudPrestamo.objects.all()
    serializer_class = SolicitudPrestamoSerializer
    
    #def get(self, request, *args, **kwargs):
    #    return self.list(request, *args, **kwargs)
    #def post
    #delete
    #devolver el mismo body que persisti
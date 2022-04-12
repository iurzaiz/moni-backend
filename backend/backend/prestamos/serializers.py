from rest_framework import serializers
from .models import SolicitudPrestamo

class SolicitudPrestamoSerializer(serializers.ModelSerializer):
    class Meta:                     # En esta clase defino el modelo con el que voy a trabajar y con que campo
        model = SolicitudPrestamo   # Con esto le indico la clase con que voy a trabajar
        fields= '__all__'           # Con esto le indico que voy a trabajar con todos los campos
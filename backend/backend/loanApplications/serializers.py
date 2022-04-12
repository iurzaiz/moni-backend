from rest_framework import serializers
from .models import LoanApplication

class LoanApplicationSerializer(serializers.ModelSerializer):
    class Meta:                     # En esta clase defino el modelo con el que voy a trabajar y con que campo
        model = LoanApplication   # Con esto le indico la clase con que voy a trabajar
        fields= '__all__'           # Con esto le indico que voy a trabajar con todos los campos
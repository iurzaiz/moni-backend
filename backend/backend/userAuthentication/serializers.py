from dataclasses import field
from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    #serializador de prueba, se usan para pasarle informacion a los post
    class Meta:
        model =get_user_model()
        fields="__all__"
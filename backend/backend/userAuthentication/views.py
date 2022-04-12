
from rest_framework.response import Response
from rest_framework import status, viewsets
from backend.loanApplications import permissions
from backend.userAuthentication import models
from rest_framework import mixins, generics, serializers
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated


from backend.userAuthentication import serializers

class UserViewSet(viewsets.ModelViewSet):
    # API login
    serializer_class = serializers.UserSerializer
    permissions_classes = (IsAuthenticated,)
    queryset=get_user_model().objects.all()
    
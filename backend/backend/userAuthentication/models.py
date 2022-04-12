from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    #Manager para perfiles de usuario

    def create_user(self, email, name, password=None):
        #Crear nuevo usuario
        if not email:
            raise ValueError("Usuario debe tener un email")
        email = self.normalize_email(email)
        user= self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, name, password):

        user = self.create_user(email, name, password)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)

        return user

    

class UserProfile(AbstractBaseUser, PermissionsMixin):
    #Modelo base de datos para usuarios del sistema
    email = models.EmailField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    
    objects = UserProfileManager()
    USERNAME_FIELD="email"
    REQUIRED_FIELDS= ["name"]

    def get_full_name(self):
        #obtengo el nombre completo
        return self.name
    def get_short_name(self):
        #obtengo el nombre corto del usuario
        return self.name

    def __str__(self) -> str:
        #obtengo nombre de usuario
        return self.email
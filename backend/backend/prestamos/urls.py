from django.urls import path
from rest_framework import routers
from . import views



urlpatterns = [
    #path('gestionSolicitudes/', views.solicitudes),
    path('', views.home),
    path('registrarSolicitud/',views.registrarSolicitud),
    path('eliminarSolicitud/<dni>',views.eliminarSolicitud),
    path('editarSolicitud/',views.editarSolicitud),
    path('edicionSolicitud/<dni>',views.edicionSolicitud),
    path('loginPage/', views.loginPage),
    path('login/', views.loginMio),

    path('solicitudes/', views.SolicitudPrestamoApiView.as_view()),
    path('solicitudes/<pk>', views.SolicitudDetalleApiView.as_view()),

]
 
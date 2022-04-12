from django.urls import path
from . import views



urlpatterns = [
    path('solicitudes/', views.SolicitudPrestamoApiView.as_view()),
    path('solicitudes/<pk>', views.SolicitudDetalleApiView.as_view()),
]
 
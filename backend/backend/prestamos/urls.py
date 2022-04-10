from django.urls import path
from rest_framework import routers
from .views import SolicitudPrestamoViewSet

router= routers.SimpleRouter()      # Esta clase va a definir las rutas para nuestro modelo, define las rutas get, post put, delete, etc
router.register('solicitudes', SolicitudPrestamoViewSet)

urlpatterns = router.urls

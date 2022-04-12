from django.test import TestCase

from backend.backend.loanApplications.models import SolicitudPrestamo

# Create your tests here.

class LoanApplicationTestCase(TestCase):
    def setUp(self):
        self.loanApplication = SolicitudPrestamo.objects.create(
            dni = "12345678",
            nombre = "imanol",
            apellido = "urzaiz",
            email = "imanol@gmail.com",
            genero = "Hombre",
            monto = "10000",)

    def test_application_creation(self):
        assert self.loanApplication.estaAprobado
    
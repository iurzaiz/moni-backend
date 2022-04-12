from django.db import models

# Creo la clase SolicitudPrestamo el cual va a tener dni, nombre y apellido, genero, email y monto solicitado.
class LoanApplication(models.Model):
    dni = models.IntegerField(null=False)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)        #Codificar esto asi no queda como string
    email = models.EmailField(max_length=50)
    monto = models.IntegerField(null=False)
    estaAprobado= models.BooleanField(default=False)

    def __str__(self) -> str:
        if (self.estaAprobado!= True):
            estado = "No aprobado"
        else:
            estado = "Aprobado"
        string= 'Nombre' + self.nombre + ' ' + self.apellido + '\n' + \
                'Monto solicitado:'+ str(self.monto) + '\n' + \
                'Estado:' + estado
        return string
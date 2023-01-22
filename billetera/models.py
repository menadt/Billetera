from django.db import models
from django.contrib.auth.models import User

# Create your models here.    
#class Cuenta(models.Model):
#    saldo = models.IntegerField()
#    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

#    def __str__(self):
#        return self.usuario.username    

class Movimiento(models.Model):
    TIPO_CHOICES=[
        ('Ingreso', 'Ingreso'),
        ('Egreso', 'Egreso')

    ]
    detalle = models.CharField(max_length=100)
    monto = models.IntegerField()
    tipo = models.CharField(choices=TIPO_CHOICES, max_length=15)
    cuenta = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.detalle + " - " + self.cuenta.username
    

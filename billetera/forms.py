from django.forms import ModelForm
from .models import Movimiento

class formCrearMovimiento(ModelForm):
    
    class Meta:
        model = Movimiento
        fields = ["detalle","monto", "tipo"]

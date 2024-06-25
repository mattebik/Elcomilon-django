from django.forms import ModelForm
from Control.models import Cliente

class Formulario1(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellidos', 'RUT', 'mail', 'telefono', 'direccion']
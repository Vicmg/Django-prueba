from django import forms
from .models import Persona
#este forms.py sirve para personalizar los templates en este caso registar un nuevo empleado 
class EmpleadoForm(forms.ModelForm):

    class Meta:
        model = Persona
        fields = (
            'first_name',
            'last_name',
            'job',
            'departamento',
            'avatar',
            'habilidades',
        )
        #con este widgets hace q las habilidades tenga  check para escoger
        widgets = {
            'habilidades': forms.CheckboxSelectMultiple()
        }
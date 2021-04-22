from django import forms# se importa el form

from .models import Prueba # se importa el modelo que tiene los campos

class PruebaForm(forms.ModelForm): #crea la clase del form

    class Meta:
        model = Prueba #se llama el modelo dela BD
        fields = (# los atributos de la BD
            "titulo",
            "subtitulo",
            "cantidad",
        )
    def clean_cantidad(self): # se crea el metodo  que valida los campos
        cantidad = self.cleaned_data["cantidad"]
        if cantidad < 10:# segenera una condicion para el campo
            raise forms.ValidationError("Ingrese un valor mayor de 10")# y el mensaje dado el error

        return cantidad


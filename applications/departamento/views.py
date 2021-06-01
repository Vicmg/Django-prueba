from django.shortcuts import render
from django.views.generic.edit import FormView

from applications.persona.models import Persona #se importa el modelo Persona
from .models import Departamento
from .forms import NewDepartamentoForm

# Create your views here.

class NewDepartamentoView (FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm #se enruta con el forms.py creado
    success_url = '/'

    def form_valid(self, form): #metodo para validar el formulario
        print("Form Valid")
        depart = Departamento( # se crea una instacia por q es una llave foranea
            name = form.cleaned_data['departamento'],  #se llama los atributos del modelo departamento
            short_name = form.cleaned_data['shorname'] # ""
        )
        depart.save()#guarda en la base datos del modelo Departamento

        nombre = form.cleaned_data['nombre'] #captura lo que viene en el formulario (forms.py)
        apellido = form.cleaned_data['apellido']
        Persona.objects.create( #se crean los campos para crar un registro del modelo empleado
            first_name = nombre,
            last_name = apellido,
            job = '1',
            departamento = depart # se reasigna a la variable de la instancia q se creó
        )
        return super(NewDepartamentoView, self).form_valid(form)
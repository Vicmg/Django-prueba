from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView
from applications.persona.models import Persona #se importa el modelo Persona
from .models import Departamento
from .forms import NewDepartamentoForm

'''El Formview trabaja con formularios que no estan vinculados con un modelo
directamente pero trabaja con mas de  un  modelo a su ves'''

class DepartamentoListView(ListView):
    template_name ='departamento/lista.html'
    model = Departamento
    context_object_name = 'departamentos'

class NewDepartamentoView (FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm #se enruta con el forms.py creado
    success_url = '/'

    def form_valid(self, form): #metodo para validar el formulario
        print("Form Valid")
        #datos del depar
        depart = Departamento( # se crea una instacia porq es una llave foranea
            name = form.cleaned_data['departamento'],  #se llama los atributos del modelo departamento
            short_name = form.cleaned_data['shorname'] # ""
        )
        depart.save()#guarda en la base datos del modelo Departamento

        nombre = form.cleaned_data['nombre'] #captura lo que viene en el formulario (forms.py)
        apellido = form.cleaned_data['apellido']
        Persona.objects.create( #se crean los campos para crar un registro del modelo Persona
            first_name = nombre,
            last_name = apellido,
            job = '1',
            departamento = depart # se crea una instancia ya que departamento pertenece a otra tabla como forenkey
        )
        return super(NewDepartamentoView, self).form_valid(form)
        #comentario views
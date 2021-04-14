from django.shortcuts import render
from django.views.generic import (ListView, DetailView, CreateView)
from .models import Persona

# Create your views here.

# 1. Listar todos los empleados de la Empresa 

class ListAllEmpleados(ListView):
    # atributos
    template_name = "persona/list_all.html"
    paginate_by = 4
    model = Persona
    
# 2. Listar todos los empleados que pertenecen al area de una empresa   

class ListByAreaEmpleado (ListView):
    """ Lista de empleados de un area"""
    template_name = 'persona/list_by_area.html'     
    
    def get_queryset(self):
        area = self.kwargs['shortname']
        lista =  Persona.objects.filter (  #Filtro  indica con que caracteristica en particular devuelva una lista 
            departamento__short_name = area
        )
        return lista

# 3. Listar todos los empleados por trabajo 
class ListByJobEmpleado (ListView):
    """ Lista de empleados por trabajo"""
    template_name = 'persona/list_job.html'
    def get_queryset(self):

        lista = Persona.objects.filter(
            job = ''
        )
        return lista

# 4. Listar los empleados por pabalabra clave 
class ListEmpleadosByKword(ListView):
    template_name = 'persona/by_word.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        print ('************************')
        palabra_clave = self.request.GET.get("kword", "")# este metodo que captura todas las solicitudes q han enviado al servidor
        lista =  Persona.objects.filter(  # aqui busca la solicitud en el modelo
            first_name = palabra_clave
        )
        print('Lista de resultad :', lista)
        return lista

# 5. Listar habilidades de un empleado many_to_may

class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        
        persona = Persona.objects.get(id=1)#para retornar un valor de many_to_many hay q indicar un valor inicial 
        return persona.habilidades.all()

    def get_queryset(self):
        id_clave = self.request.GET.get("kword", "")# este metodo que captura todas las solicitudes q han enviado al servidor
        lista =  Persona.objects.filter(  # aqui busca la solicitud en el modelo
            id = id_clave
        )
        print('Lista de resultad :', lista)
        return lista

class EmpleadoDetailView(DetailView):
    model = Persona
    template_name = "persona/detailview.html"
    
    '''para enviar una variable extra al template, una variable q no se contemple dentro de los atributos del modelo '''
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo']='Empleado del mes'
        return context
    
class EmpleadoCreateView(CreateView): # funciona co mo un formulario se usa tres parametros model,template_name,fields
    model = Persona
    template_name = "persona/add.html"
    fields = ('__all__')
    

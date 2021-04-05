from django.shortcuts import render
from django.views.generic import (ListView)
from .models import Persona

# Create your views here.

# 1. Listar todos los empleados de la Empresa 

class ListAllEmpleados(ListView):
    # atributos
    template_name = "persona/list_all.html"
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

# 2. Listar todos los empleados por trabajo 
class ListByJobEmpleado (ListView):
    """ Lista de empleados por trabajo"""
    template_name = 'persona/list_job.html'
    def get_queryset(self):

        lista = Persona.objects.filter(
            job = ''
        )
        return lista

# 2. Listar los empleados por pabalabra clave 
class ListEmpleadosByKword(ListView):
    template_name = 'persona/by_word.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        print ('************************')
        palabra_clave = self.request.GET.get("kword", "")
        lista =  Persona.objects.filter(  
            first_name = palabra_clave
        )
        print('Lista de resultad :', lista)
        return lista
        
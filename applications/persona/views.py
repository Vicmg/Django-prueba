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
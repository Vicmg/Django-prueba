from django.shortcuts import render
from django.views.generic import (ListView)
from .models import Persona

# Create your views here.

# 1. Listar todos los empleados de la Empresa 

class ListAllEmpleados(ListView):
    # atributos
    template_name = "persona/list_all.html"
    model = Persona
    context_object_name = 'lista'

# 2. Listar todos los empleados que pertenecen al area de una empresa   

class ListByAreaEmpleado (ListView):
    """ Lista de empleados de un area"""
    template_name = 'persona/list_by_area.html'     
    queryset = Persona.objects.filter (
        asociacion = 'Contabilidad'
    )

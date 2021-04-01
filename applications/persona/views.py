from django.shortcuts import render
from django.views.generic import (ListView)
from .models import Persona

# Create your views here.

# 1. Listar todos los empleados de la Empresa 

class ListAllEmpleados(ListView):
    # atributos
    template_name = "persona/list_all.html"
    model = Persona


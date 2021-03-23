from django.contrib import admin
from django.urls import path, re_path, include

def DesdePersona(self):
    print("=========Desde Apss Persona===========")
    
urlpatterns = [
    # Incluimos las urls de la app departamento 
    path('persona/',DesdePersona),
]
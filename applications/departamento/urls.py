from django.contrib import admin
from django.urls import path

def DesdeApps(self):
    print("============Desde Apps Departamento===========")

urlpatterns = [
    path('departamento/', DesdeApps)  
]

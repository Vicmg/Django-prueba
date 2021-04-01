from django.contrib import admin
from django.urls import path, re_path, include


urlpatterns = [
    path('admin/',admin.site.urls),  
    # Incluimos las urls de la app departamento 
    re_path('', include('applications.departamento.urls')),
    re_path('', include('applications.home.urls')),
    re_path('', include('applications.persona.urls')),
    
    
]

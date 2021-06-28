from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings # importamos el settings ya q ahi esta la configuracion
from django.conf.urls.static import static#nos ayuda a generar url staticas

urlpatterns = [
    path('admin/',admin.site.urls),
    # Incluimos las urls de la app departamento
    re_path('', include('applications.departamento.urls')),
    re_path('', include('applications.home.urls')),
    re_path('', include('applications.persona.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#estos pasos son para mostrar la imagen en el proyecto
#se concatena el pakete static con MEDIA_URL
#Genere una url para la ruta del documetno donde se encuentra la ruta de la carpeta
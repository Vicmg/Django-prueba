from django.contrib import admin
from .models import Persona,Habilidades
# Register your models here.


admin.site.register(Habilidades)

#decoradores para retornar cambios

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'departamento',
        'job'
    )

    search_fields = ('first_name',)
    list_filter = ('job','habilidades')

    filter_horizontal = ('habilidades',) # buscador de muchos a muchos

admin.site.register(Persona,EmpleadoAdmin)
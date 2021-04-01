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
        'job',
        'full_name',
    )

    def full_name (self, obj):
        print(obj.first_name)
        return obj.first_name + ' ' + obj.last_name

    search_fields = ('first_name',)
    list_filter = ('departamento','job','habilidades')

    filter_horizontal = ('habilidades',) # buscador de muchos a muchos

admin.site.register(Persona,EmpleadoAdmin)
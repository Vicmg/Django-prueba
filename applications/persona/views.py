from django.shortcuts import render
from django.views.generic import (ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from .models import Persona
#forms para personalizar nuevo empleado 
from .forms import EmpleadoForm # es como se llama la clase que se creo en forms.py
# vista de pagina de inicio de pantalla

class inicioView(TemplateView):
    template_name = 'inicio.html'


# 1. Listar y buscar todos los empleados de la Empresa

class ListAllEmpleados(ListView):
    # atributos
    template_name = "persona/list_all.html"
    paginate_by = 4

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", "")# este metodo que captura todas las solicitudes q han enviado al servidor
        lista =  Persona.objects.filter(  # aqui busca la solicitud en el modelo
            #el icontains sirve para encontrar similitudes en la cadena que se le ingresa
            #ejemplo : Victor = Vic
            first_name__icontains=palabra_clave
        )
        return lista

# 2. Listar todos los empleados que pertenecen al area de una empresa

class ListByAreaEmpleado (ListView):
    """ Lista de empleados de un area"""
    template_name = 'persona/list_by_area.html'
    context_object_name = 'empleados'# es un atributo que redefine el object_list y usa una varaible de contextexto para diferenciar 

    def get_queryset(self):
        area = self.kwargs['shortname']
        lista =  Persona.objects.filter (  #Filtro  indica con que caracteristica en particular devuelva una lista
            departamento__short_name = area
        )
        return lista

# Vista logica del template admin
class ListEmpleadosAdmin (ListView):

    template_name = 'persona/lista_empleados.html'
    paginate_by = 10
    ordering = "first_name"
    context_object_name = 'empleados'# es un atributo que redefine el object_list y usa una varaible de contextexto para diferenciar 
    model = Persona


# 3. Listar todos los empleados por trabajo
class ListByJobEmpleado (ListView):
    """ Lista de empleados por trabajo"""
    template_name = 'persona/list_job.html'
    def get_queryset(self):

        lista = Persona.objects.filter(
            job = ''
        )
        return lista

# 4. Listar los empleados por pabalabra clave
class ListEmpleadosByKword(ListView):
    template_name = 'persona/by_word.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        print ('************************')
        palabra_clave = self.request.GET.get("kword", "")# este metodo que captura todas las solicitudes q han enviado al servidor
        lista =  Persona.objects.filter(  # aqui busca la solicitud en el modelo
            first_name = palabra_clave
        )
        print('Lista de resultad :', lista)
        return lista

# 5. Listar habilidades de un empleado many_to_may

class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):

        persona = Persona.objects.get(id=1)#para retornar un valor de many_to_many hay q indicar un valor inicial
        return persona.habilidades.all()

    def get_queryset(self):
        id_clave = self.request.GET.get("kword", "")# este metodo que captura todas las solicitudes q han enviado al servidor
        lista =  Persona.objects.filter(  # aqui busca la solicitud en el modelo
            id = id_clave
        )
        print('Lista de resultad :', lista)
        return lista

class EmpleadoDetailView(DetailView):
    model = Persona
    template_name = "persona/detailview.html"
    '''para enviar una variable extra al template, una variable q no se contemple dentro de los atributos del modelo '''
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo']='Empleado del mes'
        return context

# controlador de empleado agregado
class SuccessView(TemplateView):
    template_name = "persona/success.html"

# controlador para crear un empleado y guardarlo en el modelo
class EmpleadoCreateView(CreateView): # se usa 4 parametros model,template_name,fields,succes(redirecciona)
    template_name = "persona/add.html"
    model = Persona
    form_class = EmpleadoForm #redirige a la clase q creamos en el forms.py
    # __all__ trae todos los atributos del modelo
    success_url = reverse_lazy("persona_app:empleados_admin")#redirecciona la pagina una vez termine el formulario

    def form_valid(self, form):
        #logica del proceso
        empleado = form.save(commit=False)#para no hacer doble guardado, crear la instacia para empleado q va a la BD
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        print(empleado)
        return super(EmpleadoCreateView,self).form_valid(form)

# controlador para actualizar el modelo

class EmpleadoUpdateView(UpdateView):
    model = Persona
    template_name = "persona/update.html"
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades'
    ]
    success_url = reverse_lazy("persona_app:empleados_admin")

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print("++++++METODO POST+++++++")
        print (request.POST)
        print (request.POST['last_name'])
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):

        return super(EmpleadoUpdateView,self).form_valid(form)

# Borrar un empleado

class EmpleadoDeleteView(DeleteView):
    model = Persona
    template_name = "persona/delete.html"
    success_url = reverse_lazy("persona_app:empleados_admin")
    '''metodo def delete (Estudiar)'''
    # def delete(self, request, *args, **kwargs):

    #     self.object = self.get_object()
    #     print("++++++METODO Delete+++++++")
    #     self.object.delete()
    #     return super(EmpleadoDeleteView, self).post(request, *args, **kwargs)

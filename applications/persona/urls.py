from django.contrib import admin
from django.urls import path, re_path, include

from  . import views

app_name = "persona_app"

urlpatterns = [
    path('', views.inicioView.as_view(), name='inicio'),
    path('listar-todo-empleados/', views.ListAllEmpleados.as_view(), name='all_empleados'),
    path('listar-by-area/<shortname>', views.ListByAreaEmpleado.as_view(), name = 'empleados_area'),
    path('lista-empleados-admin', views.ListEmpleadosAdmin.as_view(), name = 'empleados_admin'),
    path('listar-by-job/', views.ListByJobEmpleado.as_view()),
    path('buscar-empleado/', views.ListEmpleadosByKword.as_view()),
    path('listar-habilidades/', views.ListHabilidadesEmpleado.as_view()),
    path('ver.empleado/<pk>', views.EmpleadoDetailView.as_view(), name = 'empleado_detail'),# se agrega un parametro <pk> identificador para indicarle que esta relacionado con el modelo
    path('add-empleado', views.EmpleadoCreateView.as_view(), name='empleado_add'),
    path(
        'success',
        views.SuccessView.as_view(),
        name= 'correcto'),
    path(
        'update-empleado/<pk>/',
        views.EmpleadoUpdateView.as_view(),
        name= 'modificar_empleado'),
    path(
        'delete-empleado/<pk>/',
        views.EmpleadoDeleteView.as_view(),
        name= 'eliminar_empleado'),
]
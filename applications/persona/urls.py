from django.contrib import admin
from django.urls import path, re_path, include

from  . import views

urlpatterns = [
    path('listar-todo-empleados/', views.ListAllEmpleados.as_view()),
    path('listar-by-area/<shortname>', views.ListByAreaEmpleado.as_view()),
]
from django.db import models
#
from applications.departamento.models import Departamento # traer el forenkey a la tabla de partamento relacion (1-*)

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural ='Habilidades Empleados'

    def __str__(self):
        # pylint: disable=maybe-no-member
        return  str(self.id) + '-' + self.habilidad
    
class Persona (models.Model):
    """ modelo para tabla empleado """
    
    #consta de iterables de exactamente dos elementos
    JOB_CHOICES = (
        ('0', 'CONTADOR'),
        ('0', 'ADMINISTRADOR'),
        ('0', 'ECONOMISTA'),
        ('0', 'OTRO'),
    ) 
       
    first_name = models.CharField('Nombre', max_length=60) 
    last_name = models.CharField('Apellido', max_length=60)
    job = models.CharField('Trabajo', max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)# traer el forenkey a la tabla de partamento relacion (1-*)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)# relacion de muchos a muchos 
    
    class Meta:
        verbose_name = 'Mi Empleado'
        verbose_name = 'Empleados de la Empresa'
        ordering = ['-first_name', 'last_name']
        unique_together = ('first_name', 'departamento')
        
    def __str__(self):
    # pylint: disable=maybe-no-member
        return  str(self.id) + '-' + self.first_name + '-' + self.last_name
        
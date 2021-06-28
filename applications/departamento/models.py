from django.db import models

# Create your models here.

class Departamento(models.Model):

    name = models.CharField('nombre', max_length=50, blank=True)
    short_name = models.CharField('nombre corto', max_length=20, unique=True)
    anulate = models.BooleanField('anulado', default=False)

        #decoradores
    class Meta:
        verbose_name ='mi departamento'
        verbose_name_plural = 'Areas de la Empresa'#mostrar el nombre en prural
        unique_together = ('name','short_name')
        ordering = ['name']


    def __str__(self):
        # pylint: disable=maybe-no-member
        return  str(self.id) + '-' + self.name + '-' + self.short_name

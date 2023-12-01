from django.db import models

# Create your models here.

class Fornecedores(models.Model):
    
    nomeEmpresa = models.CharField('Nome', max_length=50)
    listaMateriais = models.TextField('Materiais', max_length=100)
    preços = models.TextField('Preços', max_length=100) 

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
        ordering =['id']

    def __str__(self):
        return self.name
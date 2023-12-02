from django.db import models
from fornecedores.models import Fornecedor
# Create your models here.

class Material(models.Model):
    namematerial = models.CharField('Nome do material', max_length=50)
    quantidade = models.TextField('Quantidade', max_length=100)

    
    class Meta:
        verbose_name = 'Material'
        verbose_name_plural = 'Materiais'
        ordering =['id']

    def __str__(self):
        return self.name

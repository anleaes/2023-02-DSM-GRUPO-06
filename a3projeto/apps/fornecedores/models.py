from django.db import models

# Create your models here.

class Fornecedor(models.Model):
    nomeEmpresa = models.CharField('Nome Empresa', max_length=50)
    preço = models.CharField('Preço', max_length=50)
    listamaterial = models.CharField('Lista mateial', max_length=50)

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
        ordering =['id']

    def __str__(self):
        return self.name



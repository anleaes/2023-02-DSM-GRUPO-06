from django.db import models
from usuarios.models import Usuario
from localizacoes.models import Localizacao
from fornecedores.models import Fornecedor

# Create your models here.

class Solicitacao(models.Model):
    nomeEmpresa = models.CharField('Nome', max_length=50)
    listaMateriais = models.ForeignKey(Materiais, on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
        ordering =['id']

    def __str__(self):
        return self.name



from django.db import models
from solicitacoes.models import Solicitacao
from orgaos.models import Orgao

# Create your models here.

class Servico(models.Model):
    nameservice = models.CharField('Nome do serviço', max_length=50)
    date = models.TextField('Data do serviço', max_length=100)
    solicitacao = models.ForeignKey(Solicitacao, on_delete=models.CASCADE)
    orgao = models.ForeignKey(Orgao, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Servicos'
        verbose_name_plural = 'Servicos'
        ordering =['id']

    def __str__(self):
        return self.name

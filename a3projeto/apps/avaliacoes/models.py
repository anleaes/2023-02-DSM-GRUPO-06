from django.db import models
from solicitacoes.models import Solicitacao

# Create your models here.

class Avaliacao(models.Model):
    classificacao = models.CharField('Classificao', max_length=50)
    comentarios = models.TextField('Comentarios', max_length=100)
    dataavaliacao = models.DateField('Data de avaliacao', max_length=100) 
    solicitacao = models.ForeignKey(Solicitacao, on_delete=models.CASCADE)



    class Meta:
        verbose_name = 'Avaliacao'
        verbose_name_plural = 'Avaliacoes'
        ordering =['id']

    def __str__(self):
        return self.name

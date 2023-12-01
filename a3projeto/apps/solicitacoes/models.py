from django.db import models
from usuarios.models import Usuario
from localizacoes.models import Localizacao

# Create your models here.

class Solicitacao(models.Model):
    nameproject = models.CharField('Nome', max_length=50)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    localizacao = models.ForeignKey(Localizacao, on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Lozalizacao'
        verbose_name_plural = 'Localizacoes'
        ordering =['id']

    def __str__(self):
        return self.name



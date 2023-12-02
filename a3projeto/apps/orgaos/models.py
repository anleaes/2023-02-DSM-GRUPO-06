from django.db import models

# Create your models here.

class Orgao(models.Model):
    nomeContratante = models.CharField('Nome Contratante', max_length=50)
    detalhesContrato = models.CharField('Contrato', max_length=50)

    class Meta:
        verbose_name = 'Orgao'
        verbose_name_plural = 'Orgaos'
        ordering =['id']

    def __str__(self):
        return self.name



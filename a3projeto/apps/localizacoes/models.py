from django.db import models

# Create your models here.

class Localizacao(models.Model):
    namelocal = models.CharField('Nome', max_length=50)
    endereco = models.TextField('Endereço', max_length=100)
    cep = models.TextField('cep', max_length=100) 

    class Meta:
        verbose_name = 'Localizacao'
        verbose_name_plural = 'Localizacoes'
        ordering =['id']

    def __str__(self):
        return self.name
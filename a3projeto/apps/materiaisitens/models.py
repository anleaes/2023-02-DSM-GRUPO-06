from django.db import models
from materiais.models import Material
from servicos.models import Servico

# Create your models here.

class Materiaisitens(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100)
    date_fabrication = models.DateField('Data Fabricacao', auto_now=False, auto_now_add=False) 
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Materiaisitens'
        verbose_name_plural = 'Materiaisitens'
        ordering =['id']

    def __str__(self):
        return self.name

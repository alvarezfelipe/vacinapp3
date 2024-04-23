from django.db import models

from vacina.models import Vacina
from clientes.models import Crianca
from unidade_saude.models import UnidadeSaude

# Create your models here.
class CadastroVacinal(models.Model):
    status_vacinacao = [
        ('Processamento', 'Processamento'),
        ('Completo', 'Completo'),
        ('Recusado', 'Recusado'),
    ]

    vacina = models.ForeignKey(Vacina, on_delete=models.CASCADE)
    lote = models.CharField('Lote', max_length=250, blank=True)
    fabricante = models.CharField('Fabricante', max_length=250, blank=True)
    paciente = models.ForeignKey(Crianca, on_delete=models.CASCADE)
    unidade_saude = models.ForeignKey(UnidadeSaude, on_delete=models.CASCADE)
    data_aplicacao = models.DateField('Data da aplicação')
    status = models.CharField('Status', choices=status_vacinacao, max_length=250)

    class Meta:
        db_table = 'vacinacao'
        verbose_name = 'vacinacao'
        verbose_name_plural = 'vacinacao'    
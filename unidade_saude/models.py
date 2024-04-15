from django.db import models
from localflavor.br.models import BRCNPJField, BRPostalCodeField, BRStateField

# Create your models here.
class UnidadeSaude(models.Model):
    tipo_unidade = [
        ('Upa', 'Upa'),
        ('Ubs', 'Ubs'),
        ('Hospital', 'Hospital'),
        ('Maternidade', 'Maternidade'),
    ]

    uni_cnes = models.CharField('CNES', max_length=250)
    uni_nome = models.CharField('Nome', max_length=250)
    uni_cnpj = BRCNPJField('CNPJ')
    uni_endereco = models.CharField('Endereço', max_length=250)
    uni_num_casa = models.CharField('Número', max_length=250)
    uni_bairro = models.CharField('Bairro', max_length=250)
    uni_cidade = models.CharField('Cidade', max_length=250)
    uni_uf = BRStateField('UF')
    uni_cep = BRPostalCodeField('CEP')
    uni_email = models.EmailField('Email')
    uni_tipo = models.CharField('Tipo', max_length=50, choices=tipo_unidade)

    class Meta:
        db_table = 'unidade_saude'
        ordering = ('uni_cnes',)
        verbose_name = 'unidade_saude'
        verbose_name_plural = 'unidade_saude'

    def __str__(self):
        return self.uni_nome
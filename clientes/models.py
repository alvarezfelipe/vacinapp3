from django.db import models
from localflavor.br.models import BRCPFField, BRPostalCodeField, BRStateField

# Create your models here.
class Pais(models.Model):
    pai_nome = models.CharField("Nome Completo", max_length=250)
    pai_rg = models.CharField
    pai_cpf = BRCPFField('CPF')
    pai_celular = models.CharField('Celular', max_length=15)
    pai_cep = BRPostalCodeField('CEP')
    pai_endereco = models.CharField('Endereço', max_length=250)
    pai_num_casa = models.CharField('Número', max_length=250)
    pai_complemento_casa = models.CharField('Complemento', max_length=250, blank=True)
    pai_bairro = models.CharField('Bairro', max_length=250)
    pai_cidade = models.CharField('Cidade', max_length=250)
    pai_uf = BRStateField('UF')
    pai_email = models.EmailField('Email')

    class Meta:
        db_table = "pais"
        ordering = ('pai_nome',)
        verbose_name = "pais"
        verbose_name_plural = "pais"

    def __str__(self):
        return self.pai_nome
    
class Crianca(models.Model):
    crianca_nome = models.CharField('Nome da criança', max_length=250)
    crianca_nascimento = models.DateField('Data de nascimento')
    crianca_rg = models.CharField('RG da criança', max_length=250, blank=True)
    crianca_cpf = BRCPFField('CPF', blank=True)
    crianca_responsavel = models.ForeignKey(Pais, on_delete=models.CASCADE)

    class Meta:
        db_table = "crianca"
        ordering = ("crianca_nome",)

    def __str__(self):
        return self.crianca_nome
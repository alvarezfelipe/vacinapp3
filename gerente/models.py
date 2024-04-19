from django.db import models
from localflavor.br.models import BRCPFField, BRPostalCodeField, BRStateField

# Create your models here.
class Gerente(models.Model):
    gerente_nome = models.CharField("Nome Completo", max_length=250)
    gerente_matricula = models.CharField("Matrícula", max_length=250)
    gerente_cpf = BRCPFField('CPF')
    gerente_celular = models.CharField('Celular', max_length=15)    
    gerente_email = models.EmailField('Email')

    class Meta:
        db_table = "gerentes"
        ordering = ('gerente_nome',)
        verbose_name = "gerentes"
        verbose_name_plural = "gerentes"

    def __str__(self):
        return self.gerente_nome

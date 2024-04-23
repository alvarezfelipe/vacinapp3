from django.db import models

# Create your models here.
class Vacina(models.Model):
    vacina_nome = models.CharField('Vacina', max_length=250)
    vacina_lote = models.CharField('Lote', max_length=250, blank=True)
    vacina_fabricante = models.CharField('Lote', max_length=250, blank=True)

    def __str__(self):
        return self.vacina_nome
    
class CalendarioVacina(models.Model):
    dose_choices = [
        ('1ª dose', '1ª dose'), 
        ('2ª dose', '2ª dose'), 
        ('3ª dose', '3ª dose'), 
        ('4ª dose', '4ª dose'), 
        ('6ª dose', '6ª dose'), 
        ('dose unica', 'dose unica'), 
        ('reforço', 'reforço'), 
    ]

    calendario_vacina = models.ForeignKey(Vacina, on_delete=models.CASCADE)
    calendario_dose = models.CharField('Dose', max_length=20, choices=dose_choices)
    calendario_idade = models.CharField('Idade', max_length=20)
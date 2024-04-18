from django.contrib import admin
from .models import *

# Register your models here.
class VacinacaoAdmin(admin.ModelAdmin):
    list_display = (
        'data_aplicacao',
        'unidade_saude',
        'paciente',
        'vacina',        
        'status', )
    
    ordering = ('data_aplicacao',)

admin.site.register(CadastroVacinal, VacinacaoAdmin)
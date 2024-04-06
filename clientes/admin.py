from django.contrib import admin
from .models import *

# Register your models here.
class PaisAdmin(admin.ModelAdmin):
    list_display = ('pai_nome','pai_cpf','pai_celular','pai_email')
    ordering = ('pai_nome',)

class CriancaAdmin(admin.ModelAdmin):
    list_display = ('crianca_nome','crianca_nascimento','crianca_responsavel')
    ordering = ('crianca_nome',)

admin.site.register(Pais, PaisAdmin)
admin.site.register(Crianca, CriancaAdmin)
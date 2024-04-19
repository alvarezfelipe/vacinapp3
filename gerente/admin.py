from django.contrib import admin
from .models import *

# Register your models here.
class GerenteAdmin(admin.ModelAdmin):
    list_display = ('gerente_nome','gerente_cpf','gerente_celular','gerente_email')
    ordering = ('gerente_nome',)

admin.site.register(Gerente, GerenteAdmin)
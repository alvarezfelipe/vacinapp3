from django.contrib import admin
from .models import *

# Register your models here.
class VacinaAdmin(admin.ModelAdmin):
    list_display = ('vacina_nome','vacina_lote','vacina_fabricante')
    ordering = ('vacina_nome',)

class CalendarioAdmin(admin.ModelAdmin):
    list_display = ('calendario_vacina','calendario_dose','calendario_idade')
    ordering = ('calendario_vacina',)

admin.site.register(Vacina, VacinaAdmin)
admin.site.register(CalendarioVacina, CalendarioAdmin)
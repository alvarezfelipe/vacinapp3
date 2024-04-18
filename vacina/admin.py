from django.contrib import admin
from .models import Vacina

# Register your models here.
class VacinaAdmin(admin.ModelAdmin):
    list_display = ('vacina_nome','vacina_lote','vacina_fabricante')
    ordering = ('vacina_nome',)

admin.site.register(Vacina, VacinaAdmin)
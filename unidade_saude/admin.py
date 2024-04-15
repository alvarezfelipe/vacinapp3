from django.contrib import admin
from .models import *

# Register your models here.
class UniAdmin(admin.ModelAdmin):
    list_display = ('uni_nome','uni_cnes','uni_email',)
    ordering = ('uni_cnes',)

admin.site.register(UnidadeSaude, UniAdmin)
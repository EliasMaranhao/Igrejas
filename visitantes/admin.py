from django.contrib import admin
from .models import Visitante

# Register your models here.

class ListandoVisitantes(admin.ModelAdmin):
    list_display = ('nome', 'igreja_origem')
    list_display_links = ('nome',)
    search_fields = ('nome', 'data_visita')
    list_filter = ('evangelico', 'primeira_vez')
    list_per_page = 5
    

admin.site.register(Visitante, ListandoVisitantes)

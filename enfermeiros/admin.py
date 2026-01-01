from django.contrib import admin
from .models import Enfermeiro


@admin.register(Enfermeiro)
class EnfermeiroAdmin(admin.ModelAdmin):
    list_display = (
        'nome_completo',
        'cpf',
        'coren',
        'coren_uf',
        'categoria',
        'ativo',
    )
    list_filter = ('categoria', 'ativo', 'coren_uf')
    search_fields = ('nome_completo', 'cpf', 'coren', 'cns')
    ordering = ('nome_completo',)

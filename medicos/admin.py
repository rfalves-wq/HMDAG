from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Medico


@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = (
        'nome_completo',
        'crm',
        'crm_uf',
        'cbo',
        'cnes',
        'ativo',
    )

    search_fields = (
        'nome_completo',
        'cpf',
        'cns',
        'crm',
    )

    list_filter = (
        'crm_uf',
        'ativo',
        'data_cadastro',
    )

    ordering = ('nome_completo',)

    readonly_fields = (
        'data_cadastro',
        'data_atualizacao',
    )

    fieldsets = (
        ('Identificação Profissional', {
            'fields': ('cns', 'cpf')
        }),
        ('Dados Pessoais', {
            'fields': (
                'nome_completo',
                'data_nascimento',
                'sexo',
            )
        }),
        ('Registro Profissional', {
            'fields': (
                'crm',
                'crm_uf',
                'cbo',
                'especialidade',
            )
        }),
        ('Contato', {
            'fields': ('telefone', 'email')
        }),
        ('Vínculo Institucional', {
            'fields': ('cnes',)
        }),
        ('Controle', {
            'fields': (
                'ativo',
                'data_cadastro',
                'data_atualizacao',
            )
        }),
    )

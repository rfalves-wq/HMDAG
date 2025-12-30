from django.contrib import admin
from .models import Paciente


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = (
        'nome_completo',
        'cns',
        'cpf',
        'sexo',
        'data_nascimento',
        'cidade',
        'estado',
        'ativo',
    )

    search_fields = (
        'nome_completo',
        'nome_social',
        'cns',
        'cpf',
        'nome_mae',
    )

    list_filter = (
        'sexo',
        'estado',
        'ativo',
        'data_cadastro',
    )

    ordering = ('nome_completo',)

    readonly_fields = (
        'data_cadastro',
        'data_atualizacao',
    )

    fieldsets = (
        ('Identificação SUS', {
            'fields': ('cns', 'cpf')
        }),
        ('Dados Pessoais', {
            'fields': (
                'nome_completo',
                'nome_social',
                'data_nascimento',
                'sexo',
                'estado_civil',
                'nome_mae',
                'nome_pai',
            )
        }),
        ('Contato', {
            'fields': ('telefone', 'email')
        }),
        ('Endereço', {
            'fields': (
                'cep',
                'logradouro',
                'numero',
                'complemento',
                'bairro',
                'cidade',
                'estado',
            )
        }),
        ('Controle', {
            'fields': (
                'ativo',
                'data_cadastro',
                'data_atualizacao',
            )
        }),
    )

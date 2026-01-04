from django.contrib import admin
from .models import TecnicoEnfermagem


@admin.register(TecnicoEnfermagem)
class TecnicoEnfermagemAdmin(admin.ModelAdmin):

    # =====================
    # Lista
    # =====================
    list_display = (
        'nome_completo',
        'cpf',
        'cns',
        'coren',
        'coren_uf',
        'ativo',
        'data_cadastro',
    )

    list_filter = (
        'ativo',
        'sexo',
        'estado_civil',
        'uf',
        'coren_uf',
    )

    search_fields = (
        'nome_completo',
        'nome_social',
        'cpf',
        'cns',
        'coren',
    )

    ordering = ('nome_completo',)

    # =====================
    # Organização do formulário
    # =====================
    fieldsets = (
        ('Identificação', {
            'fields': (
                'nome_completo',
                'nome_social',
                'cpf',
                'cns',
                'data_nascimento',
                'sexo',
                'estado_civil',
                'nome_mae',
                'nome_pai',
            )
        }),
        ('Contato', {
            'fields': (
                'telefone',
                'email',
            )
        }),
        ('Endereço', {
            'fields': (
                'cep',
                'logradouro',
                'numero',
                'complemento',
                'bairro',
                'municipio',
                'uf',
            )
        }),
        ('Dados Profissionais', {
            'fields': (
                'coren',
                'coren_uf',
                'ativo',
            )
        }),
        ('Auditoria', {
            'fields': (
                'data_cadastro',
                'data_atualizacao',
            )
        }),
    )

    readonly_fields = (
        'data_cadastro',
        'data_atualizacao',
    )

    list_per_page = 20


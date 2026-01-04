from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Medico


@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    # -----------------------------
    # LISTAGEM
    # -----------------------------
    list_display = (
        'nome_completo',
        'crm',
        'uf_crm',
        'especialidade',
        'cpf',
        'cns',
        'ativo',
    )

    list_filter = (
        'ativo',
        'especialidade',
        'uf_crm',
        'sexo',
    )

    search_fields = (
        'nome_completo',
        'cpf',
        'cns',
        'crm',
    )

    ordering = ('nome_completo',)

    # -----------------------------
    # ORGANIZAÇÃO DO FORMULÁRIO
    # -----------------------------
    fieldsets = (
        ('Identificação (SUS)', {
            'fields': (
                'cns',
                'cpf',
                'nome_completo',
                'nome_social',
                'data_nascimento',
                'sexo',
            )
        }),
        ('Dados Profissionais', {
            'fields': (
                'crm',
                'uf_crm',
                'especialidade',
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
        ('Controle', {
            'fields': (
                'ativo',
            )
        }),
        ('Auditoria', {
            'fields': (
                'criado_em',
                'atualizado_em',
            )
        }),
    )

    readonly_fields = (
        'criado_em',
        'atualizado_em',
    )

    # -----------------------------
    # MELHORIAS DE USABILIDADE
    # -----------------------------
    list_per_page = 20
    save_on_top = True

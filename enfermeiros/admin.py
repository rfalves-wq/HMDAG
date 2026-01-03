from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Enfermeiro


@admin.register(Enfermeiro)
class EnfermeiroAdmin(admin.ModelAdmin):

    list_display = (
        'nome_completo',
        'cns',
        'cpf',
        'coren',
        'uf_coren',
        'estabelecimento_cnes',
        'ativo',
    )

    list_filter = (
        'ativo',
        'sexo',
        'uf',
        'uf_coren',
    )

    search_fields = (
        'nome_completo',
        'nome_social',
        'cpf',
        'cns',
        'coren',
    )

    ordering = ('nome_completo',)

    list_per_page = 25

    fieldsets = (
        ('Identificação SUS', {
            'fields': (
                'cns',
                'cpf',
                'nome_completo',
                'nome_social',
                'data_nascimento',
                'sexo',
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
                'uf_coren',
                'estabelecimento_cnes',
                'ativo',
            )
        }),
        ('Controle do Sistema', {
            'fields': (
                'data_cadastro',
            )
        }),
    )

    readonly_fields = ('data_cadastro',)

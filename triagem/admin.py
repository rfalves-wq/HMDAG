from django.contrib import admin
from .models import Triagem


@admin.register(Triagem)
class TriagemAdmin(admin.ModelAdmin):
    """
    Administração de Triagens - Padrão SUS (ACCR)
    """

    # =========================
    # LISTAGEM
    # =========================
    list_display = (
        'id',
        'paciente',
        'enfermeiro',
        'classificacao_risco',
        'data_hora_triagem',
    )

    list_filter = (
        'classificacao_risco',
        'data_hora_triagem',
        'enfermeiro',
    )

    search_fields = (
        'atendimento__paciente__nome_completo',
        'queixa_principal',
    )

    date_hierarchy = 'data_hora_triagem'

    ordering = ('-data_hora_triagem',)

    # =========================
    # CAMPOS SOMENTE LEITURA
    # =========================
    readonly_fields = (
        'data_hora_triagem',
        'atendimento',
        'enfermeiro',
    )

    # =========================
    # ORGANIZAÇÃO DO FORMULÁRIO
    # =========================
    fieldsets = (
        ('Identificação', {
            'fields': (
                'atendimento',
                'enfermeiro',
                'data_hora_triagem',
            )
        }),

        ('Queixa Principal', {
            'fields': (
                'queixa_principal',
                'inicio_sintomas',
            )
        }),

        ('Sinais Vitais', {
            'fields': (
                'pressao_arterial',
                'frequencia_cardiaca',
                'frequencia_respiratoria',
                'temperatura',
                'saturacao_oxigenio',
                'dor',
            )
        }),

        ('Avaliação Clínica', {
            'fields': (
                'nivel_consciencia',
                'mobilidade',
                'sangramento',
                'dispneia',
                'dor_toracica',
                'nausea_vomito',
            )
        }),

        ('Classificação de Risco', {
            'fields': (
                'classificacao_risco',
            )
        }),

        ('Conduta e Observações', {
            'fields': (
                'conduta',
                'observacoes',
            )
        }),
    )

    # =========================
    # MÉTODOS AUXILIARES
    # =========================
    @admin.display(description='Paciente')
    def paciente(self, obj):
        return obj.atendimento.paciente

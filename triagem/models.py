from django.db import models
from recepcao.models import Atendimento
from enfermeiros.models import Enfermeiro


class Triagem(models.Model):
    """
    Modelo de Triagem baseado no Acolhimento com Classificação de Risco (ACCR - SUS)
    """

    # =========================
    # CLASSIFICAÇÃO DE RISCO
    # =========================
    CLASSIFICACAO_RISCO_CHOICES = [
        ('vermelho', 'Vermelho - Emergência'),
        ('laranja', 'Laranja - Muito Urgente'),
        ('amarelo', 'Amarelo - Urgente'),
        ('verde', 'Verde - Pouco Urgente'),
        ('azul', 'Azul - Não Urgente'),
    ]

    # =========================
    # RELACIONAMENTOS
    # =========================
    atendimento = models.OneToOneField(
        Atendimento,
        on_delete=models.CASCADE,
        related_name='triagem',
        verbose_name='Atendimento'
    )

    enfermeiro = models.ForeignKey(
        Enfermeiro,
        on_delete=models.PROTECT,
        related_name='triagens',
        verbose_name='Enfermeiro Responsável'
    )

    # =========================
    # QUEIXA PRINCIPAL
    # =========================
    queixa_principal = models.TextField(
        verbose_name='Queixa Principal'
    )

    inicio_sintomas = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Início dos Sintomas'
    )

    # =========================
    # SINAIS VITAIS
    # =========================
    pressao_arterial = models.CharField(
        max_length=7,
        verbose_name='Pressão Arterial (mmHg)',
        help_text='Ex: 120/80'
    )

    frequencia_cardiaca = models.PositiveIntegerField(
        verbose_name='Frequência Cardíaca (bpm)'
    )

    frequencia_respiratoria = models.PositiveIntegerField(
        verbose_name='Frequência Respiratória (irpm)'
    )

    temperatura = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        verbose_name='Temperatura (°C)'
    )

    saturacao_oxigenio = models.PositiveIntegerField(
        verbose_name='Saturação de O₂ (%)'
    )

    dor = models.PositiveIntegerField(
        verbose_name='Escala de Dor (0 a 10)',
        help_text='0 = sem dor | 10 = pior dor possível'
    )

    # =========================
    # AVALIAÇÃO CLÍNICA
    # =========================
    nivel_consciencia = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='Nível de Consciência'
    )

    mobilidade = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='Mobilidade'
    )

    sangramento = models.BooleanField(
        default=False,
        verbose_name='Presença de Sangramento'
    )

    dispneia = models.BooleanField(
        default=False,
        verbose_name='Dispneia'
    )

    dor_toracica = models.BooleanField(
        default=False,
        verbose_name='Dor Torácica'
    )

    nausea_vomito = models.BooleanField(
        default=False,
        verbose_name='Náusea/Vômito'
    )

    # =========================
    # CLASSIFICAÇÃO E CONDUTA
    # =========================
    classificacao_risco = models.CharField(
        max_length=10,
        choices=CLASSIFICACAO_RISCO_CHOICES,
        verbose_name='Classificação de Risco'
    )

    conduta = models.TextField(
        blank=True,
        verbose_name='Conduta/Encaminhamento'
    )

    observacoes = models.TextField(
        blank=True,
        verbose_name='Observações'
    )

    # =========================
    # CONTROLE DE TEMPO
    # =========================
    data_hora_triagem = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data/Hora da Triagem'
    )

    # =========================
    # METADADOS
    # =========================
    class Meta:
        verbose_name = 'Triagem'
        verbose_name_plural = 'Triagens'
        ordering = ['-data_hora_triagem']

    def __str__(self):
        return f'Triagem - {self.atendimento.paciente} ({self.get_classificacao_risco_display()})'

from django.db import models
from pacientes.models import Paciente
from enfermeiros.models import Enfermeiro
PRIORIDADE_CHOICES = [
    ('vermelho', 'Vermelho (emergência)'),
    ('amarelo', 'Amarelo (alta)'),
    ('verde', 'Verde (média)'),
    ('azul', 'Azul (baixa)'),
]

class Triagem(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    enfermeiro = models.ForeignKey(Enfermeiro, on_delete=models.SET_NULL, null=True, blank=True)
    data_hora = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('aguardando', 'Aguardando Atendimento'),
        ('em_atendimento', 'Em Atendimento'),
        ('concluida', 'Concluída')
    ], default='aguardando')

    prioridade = models.CharField(max_length=10, choices=PRIORIDADE_CHOICES, default='verde')

    # Campos de sinais vitais
    pressao_arterial = models.CharField(max_length=10, blank=True, null=True)
    frequencia_cardiaca = models.IntegerField(blank=True, null=True)
    temperatura = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    frequencia_respiratoria = models.IntegerField(blank=True, null=True)
    saturacao_oxigenio = models.IntegerField(blank=True, null=True)
    queixa_principal = models.TextField(blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.paciente.nome_completo} - {self.get_prioridade_display()}"

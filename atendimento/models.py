from django.db import models

# Create your models here.
from django.db import models
from pacientes.models import Paciente
from medicos.models import Medico  # Se você já tem o app medicos

class AtendimentoMedico(models.Model):
    STATUS_CHOICES = [
        ('aguardando', 'Aguardando'),
        ('em_consulta', 'Em Consulta'),
        ('concluido', 'Concluído'),
    ]

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.SET_NULL, null=True)
    queixa_principal = models.TextField()
    diagnostico = models.TextField(blank=True, null=True)
    prescricao = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='aguardando')

    def __str__(self):
        return f"{self.paciente.nome_completo} - {self.status}"

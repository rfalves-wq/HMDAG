from django.db import models

# Create your models here.
from django.db import models
from pacientes.models import Paciente
from enfermeiros.models import Enfermeiro

class Atendimento(models.Model):

    STATUS_CHOICES = [
        ('aguardando_triagem', 'Aguardando Triagem'),
        ('em_triagem', 'Em Triagem'),
        ('triado', 'Triado'),
        ('finalizado', 'Finalizado'),
    ]

    paciente = models.ForeignKey(
        Paciente,
        on_delete=models.CASCADE,
        related_name='atendimentos'
    )

    enfermeiro = models.ForeignKey(
        Enfermeiro,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    data_hora_chegada = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default='aguardando_triagem'
    )

    observacoes = models.TextField(blank=True)

    class Meta:
        ordering = ['data_hora_chegada']

    def __str__(self):
        return f"{self.paciente.nome_completo} - {self.get_status_display()}"

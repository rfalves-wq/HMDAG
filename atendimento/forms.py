from django import forms
from .models import AtendimentoMedico

class AtendimentoMedicoForm(forms.ModelForm):
    class Meta:
        model = AtendimentoMedico
        fields = ['paciente', 'medico', 'queixa_principal', 'diagnostico', 'prescricao', 'status']

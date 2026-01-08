from django import forms
from .models import Triagem

class TriagemForm(forms.ModelForm):
    class Meta:
        model = Triagem
        fields = [
            'pressao_arterial',
            'frequencia_cardiaca',
            'temperatura',
            'frequencia_respiratoria',
            'saturacao_oxigenio',
            'queixa_principal',
            'observacoes',
        ]
        widgets = {
            'queixa_principal': forms.Textarea(attrs={'rows': 3}),
            'observacoes': forms.Textarea(attrs={'rows': 2}),
        }

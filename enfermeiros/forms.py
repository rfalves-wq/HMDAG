from django import forms
from .models import Enfermeiro


class EnfermeiroForm(forms.ModelForm):
    class Meta:
        model = Enfermeiro
        fields = [
            'cns',
            'cpf',
            'nome_completo',
            'data_nascimento',
            'sexo',
            'coren',
            'coren_uf',
            'cbo',
            'categoria',
            'telefone',
            'email',
            'cnes',
            'ativo',
        ]
        widgets = {
            'data_nascimento': forms.DateInput(
                attrs={'type': 'date'}
            )
        }

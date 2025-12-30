from django import forms
from .models import Paciente


class PacienteForm(forms.ModelForm):

    data_nascimento = forms.DateField(
        widget=forms.DateInput(
            attrs={'type': 'date'}
        )
    )

    class Meta:
        model = Paciente
        fields = [
            'cns',
            'cpf',
            'nome_completo',
            'nome_social',
            'data_nascimento',
            'sexo',
            'estado_civil',
            'nome_mae',
            'nome_pai',
            'telefone',
            'email',
            'cep',
            'logradouro',
            'numero',
            'complemento',
            'bairro',
            'cidade',
            'estado',
            'ativo',
        ]

        widgets = {
            'sexo': forms.Select(attrs={'class': 'form-select'}),
            'estado_civil': forms.Select(attrs={'class': 'form-select'}),
            'ativo': forms.CheckboxInput(),
        }

    # Validação do CNS (15 dígitos)
    def clean_cns(self):
        cns = self.cleaned_data.get('cns')

        if not cns.isdigit() or len(cns) != 15:
            raise forms.ValidationError(
                "O CNS deve conter exatamente 15 dígitos numéricos."
            )

        return cns

    # Validação simples do CPF (opcional)
    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')

        if cpf:
            if not cpf.isdigit() or len(cpf) != 11:
                raise forms.ValidationError(
                    "O CPF deve conter 11 dígitos numéricos."
                )

        return cpf

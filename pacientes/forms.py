import re
from django import forms

from .models import Paciente


class PacienteForm(forms.ModelForm):

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
          'cns': forms.TextInput(attrs={
    'class': 'form-control',
    'placeholder': '000 0000 0000 0000',
    'maxlength': '18'
}),
          'cpf': forms.TextInput(attrs={
    'class': 'form-control',
    'placeholder': '000.000.000-00',
    'maxlength': '14'
}),

            # Dados pessoais
            'nome_completo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome completo'
            }),
            'nome_social': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome social'
            }),
            'data_nascimento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'sexo': forms.Select(attrs={
                'class': 'form-select'
            }),
            'estado_civil': forms.Select(attrs={
                'class': 'form-select'
            }),
            'nome_mae': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome da mãe'
            }),
            'nome_pai': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome do pai'
            }),

            # Contato
           'telefone': forms.TextInput(attrs={
    'class': 'form-control',
    'placeholder': '(00) 00000-0000',
    'maxlength': '15'
}),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'email@exemplo.com'
            }),

            # Endereço
           'cep': forms.TextInput(attrs={
    'class': 'form-control',
    'placeholder': '00000-000',
    'maxlength': '9'
}),
            'logradouro': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Rua / Avenida'
            }),
            'numero': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número'
            }),
            'complemento': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Complemento'
            }),
            'bairro': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Bairro'
            }),
            'cidade': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Cidade'
            }),
            'Estado': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Estado'
            }),

            # Status
            'ativo': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }

   

def clean_cpf(self):
    cpf = self.cleaned_data.get('cpf')

    if not cpf:
        return cpf

    # remove qualquer máscara
    numeros = re.sub(r'\D', '', cpf)

    if len(numeros) != 11:
        raise forms.ValidationError(
            "O CPF deve conter 11 dígitos."
        )

    # SALVA COM MÁSCARA NO BANCO
    cpf_formatado = (
        f"{numeros[:3]}."
        f"{numeros[3:6]}."
        f"{numeros[6:9]}-"
        f"{numeros[9:]}"
    )

    return cpf_formatado


def clean_cns(self):
    cns = self.cleaned_data.get('cns')

    if not cns:
        raise forms.ValidationError(
            "O CNS é obrigatório."
        )

    # remove qualquer máscara
    numeros = re.sub(r'\D', '', cns)

    if len(numeros) != 15:
        raise forms.ValidationError(
            "O CNS deve conter exatamente 15 dígitos."
        )

    # SALVA COM MÁSCARA NO BANCO
    cns_formatado = (
        f"{numeros[:3]} "
        f"{numeros[3:7]} "
        f"{numeros[7:11]} "
        f"{numeros[11:]}"
    )

    return cns_formatado

def clean_telefone(self):
    telefone = self.cleaned_data.get('telefone')

    if not telefone:
        return telefone

    numeros = re.sub(r'\D', '', telefone)

    if len(numeros) not in [10, 11]:
        raise forms.ValidationError(
            "O telefone deve conter 10 ou 11 dígitos."
        )

    # celular com 9 dígitos
    if len(numeros) == 11:
        return f"({numeros[:2]}) {numeros[2:7]}-{numeros[7:]}"
    # fixo
    return f"({numeros[:2]}) {numeros[2:6]}-{numeros[6:]}"

def clean_cep(self):
    cep = self.cleaned_data.get('cep')

    numeros = re.sub(r'\D', '', cep)

    if len(numeros) != 8:
        raise forms.ValidationError(
            "O CEP deve conter 8 dígitos."
        )

    # SALVA COM MÁSCARA
    return f"{numeros[:5]}-{numeros[5:]}"


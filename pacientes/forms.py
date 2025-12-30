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
            # Documentos
            'cns': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Cartão Nacional de Saúde',
                'maxlength': '15'
            }),
            'cpf': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'CPF',
                'maxlength': '11'
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
                'placeholder': '(00) 00000-0000'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'email@exemplo.com'
            }),

            # Endereço
            'cep': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '00000-000'
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

    # Validação do CNS (15 dígitos)
    def clean_cns(self):
        cns = self.cleaned_data.get('cns')

        if not cns or not cns.isdigit() or len(cns) != 15:
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



from django import forms
from .models import Medico


class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = [
            # Identificação
            'cns',
            'cpf',
            'nome_completo',
            'nome_social',
            'data_nascimento',
            'sexo',

            # Dados profissionais
            'crm',
            'uf_crm',
            'especialidade',

            # Contato
            'telefone',
            'email',

            # Endereço
            'cep',
            'logradouro',
            'numero',
            'complemento',
            'bairro',
            'municipio',
            'uf',

            # Controle
            'ativo',
        ]

        widgets = {
            'cns': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Cartão Nacional de Saúde'
            }),
            'cpf': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'CPF (somente números)'
            }),
            'nome_completo': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'nome_social': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'data_nascimento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'sexo': forms.Select(attrs={
                'class': 'form-select'
            }),
            'crm': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: 12345'
            }),
            'uf_crm': forms.Select(attrs={
                'class': 'form-select'
            }),
            'especialidade': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'telefone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '(DDD) Telefone'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control'
            }),
            'cep': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'CEP'
            }),
            'logradouro': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'numero': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'complemento': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'bairro': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'municipio': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'uf': forms.Select(attrs={
                'class': 'form-select'
            }),
            'ativo': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }

    # -----------------------------
    # VALIDAÇÕES SUS
    # -----------------------------
    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        if not cpf.isdigit() or len(cpf) != 11:
            raise forms.ValidationError("CPF deve conter 11 dígitos numéricos.")
        return cpf

    def clean_cns(self):
        cns = self.cleaned_data['cns']
        if not cns.isdigit() or len(cns) != 15:
            raise forms.ValidationError("CNS deve conter 15 dígitos numéricos.")
        return cns

    def clean_cep(self):
        cep = self.cleaned_data.get('cep')
        if cep and (not cep.isdigit() or len(cep) != 8):
            raise forms.ValidationError("CEP deve conter 8 dígitos numéricos.")
        return cep

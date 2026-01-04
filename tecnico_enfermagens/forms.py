from django import forms
from .models import TecnicoEnfermagem


class TecnicoEnfermagemForm(forms.ModelForm):

    data_nascimento = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = TecnicoEnfermagem
        fields = [
            # Identificação
            'cns',
            'cpf',
            'nome_completo',
            'nome_social',
            'data_nascimento',
            'sexo',
            'estado_civil',
            'nome_mae',
            'nome_pai',

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

            # Dados Profissionais
            'coren',
            'coren_uf',
            'ativo',
        ]

        widgets = {
            'cns': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'nome_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'nome_social': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-select'}),
            'estado_civil': forms.Select(attrs={'class': 'form-select'}),
            'nome_mae': forms.TextInput(attrs={'class': 'form-control'}),
            'nome_pai': forms.TextInput(attrs={'class': 'form-control'}),

            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),

            'cep': forms.TextInput(attrs={'class': 'form-control'}),
            'logradouro': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'complemento': forms.TextInput(attrs={'class': 'form-control'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control'}),
            'municipio': forms.TextInput(attrs={'class': 'form-control'}),
            'uf': forms.Select(attrs={'class': 'form-select'}),

            'coren': forms.TextInput(attrs={'class': 'form-control'}),
            'coren_uf': forms.Select(attrs={'class': 'form-select'}),
            'ativo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    # =====================
    # Validações SUS básicas
    # =====================

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if not cpf.isdigit() or len(cpf) != 11:
            raise forms.ValidationError("CPF deve conter 11 dígitos numéricos.")
        return cpf

    def clean_cns(self):
        cns = self.cleaned_data.get('cns')
        if not cns.isdigit() or len(cns) != 15:
            raise forms.ValidationError("CNS deve conter 15 dígitos numéricos.")
        return cns

    def clean_cep(self):
        cep = self.cleaned_data.get('cep')
        if not cep.isdigit() or len(cep) != 8:
            raise forms.ValidationError("CEP deve conter 8 dígitos numéricos.")
        return cep

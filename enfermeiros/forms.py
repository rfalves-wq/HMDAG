from django import forms
from .models import Enfermeiro


class EnfermeiroForm(forms.ModelForm):

    class Meta:
        model = Enfermeiro
        fields = [
            # Identificação SUS
            'cns',
            'cpf',
            'nome_completo',
            'nome_social',
            'data_nascimento',
            'sexo',
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
            'uf_coren',
            'estabelecimento_cnes',
            'ativo',
        ]

        widgets = {
            'data_nascimento': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}
            ),
            'sexo': forms.Select(attrs={'class': 'form-select'}),
            'uf': forms.Select(attrs={'class': 'form-select'}),
            'uf_coren': forms.Select(attrs={'class': 'form-select'}),
            'ativo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Aplica Bootstrap automaticamente
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, (forms.CheckboxInput, forms.RadioSelect)):
                field.widget.attrs.setdefault('class', 'form-control')

        # Campos obrigatórios (SUS)
        obrigatorios = [
            'cns', 'cpf', 'nome_completo', 'data_nascimento',
            'sexo', 'nome_mae', 'telefone',
            'cep', 'logradouro', 'numero', 'bairro',
            'municipio', 'uf', 'coren', 'uf_coren'
        ]

        for campo in obrigatorios:
            self.fields[campo].required = True

    # Validações específicas SUS
    def clean_cns(self):
        cns = self.cleaned_data.get('cns')
        if len(cns) != 15 or not cns.isdigit():
            raise forms.ValidationError('O CNS deve conter exatamente 15 dígitos numéricos.')
        return cns

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if cpf and (len(cpf) != 11 or not cpf.isdigit()):
            raise forms.ValidationError('O CPF deve conter exatamente 11 dígitos numéricos.')
        return cpf

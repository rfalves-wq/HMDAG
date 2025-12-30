from django import forms
from .models import Medico


class MedicoForm(forms.ModelForm):

    data_nascimento = forms.DateField(
        widget=forms.DateInput(
            attrs={'type': 'date'}
        )
    )

    class Meta:
        model = Medico
        fields = [
            'cns',
            'cpf',
            'nome_completo',
            'data_nascimento',
            'sexo',
            'crm',
            'crm_uf',
            'cbo',
            'especialidade',
            'telefone',
            'email',
            'cnes',
            'ativo',
        ]

        widgets = {
            'sexo': forms.Select(attrs={'class': 'form-select'}),
            'crm_uf': forms.Select(attrs={'class': 'form-select'}),
            'ativo': forms.CheckboxInput(),
        }

    # Validação CNS (15 dígitos)
    def clean_cns(self):
        cns = self.cleaned_data.get('cns')

        if not cns.isdigit() or len(cns) != 15:
            raise forms.ValidationError(
                "O CNS deve conter exatamente 15 dígitos numéricos."
            )

        return cns

    # Validação CPF (11 dígitos)
    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')

        if not cpf.isdigit() or len(cpf) != 11:
            raise forms.ValidationError(
                "O CPF deve conter exatamente 11 dígitos numéricos."
            )

        return cpf

    # Validação CBO (6 dígitos)
    def clean_cbo(self):
        cbo = self.cleaned_data.get('cbo')

        if not cbo.isdigit() or len(cbo) != 6:
            raise forms.ValidationError(
                "O CBO deve conter exatamente 6 dígitos numéricos."
            )

        return cbo

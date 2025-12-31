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
            'estado_civil': forms.Select(attrs={
                'class': 'form-select'
            }),
            'nome_mae': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'nome_pai': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'telefone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '(00) 00000-0000',
                'maxlength': '15'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control'
            }),
            'cep': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '00000-000',
                'maxlength': '9'
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
            'cidade': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'estado': forms.Select(attrs={
                'class': 'form-select'
            }),
            'ativo': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }

    # ================= CPF =================
    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')

        if not cpf:
            return cpf

        cpf = re.sub(r'\D', '', cpf)

        if len(cpf) != 11 or cpf == cpf[0] * 11:
            raise forms.ValidationError("CPF inválido.")

        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        resto = (soma * 10) % 11
        resto = 0 if resto == 10 else resto

        if resto != int(cpf[9]):
            raise forms.ValidationError("CPF inválido.")

        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        resto = (soma * 10) % 11
        resto = 0 if resto == 10 else resto

        if resto != int(cpf[10]):
            raise forms.ValidationError("CPF inválido.")

        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

    # ================= CNS =================
    def clean_cns(self):
        cns = self.cleaned_data.get('cns')

        if not cns:
            raise forms.ValidationError("O CNS é obrigatório.")

        numeros = re.sub(r'\D', '', cns)

        if len(numeros) != 15:
            raise forms.ValidationError("CNS inválido.")

        return f"{numeros[:3]} {numeros[3:7]} {numeros[7:11]} {numeros[11:]}"

    # ================= TELEFONE =================
    def clean_telefone(self):
        telefone = self.cleaned_data.get('telefone')

        if not telefone:
            return telefone

        numeros = re.sub(r'\D', '', telefone)

        if len(numeros) not in (10, 11):
            raise forms.ValidationError("Telefone inválido.")

        return (
            f"({numeros[:2]}) {numeros[2:7]}-{numeros[7:]}"
            if len(numeros) == 11
            else f"({numeros[:2]}) {numeros[2:6]}-{numeros[6:]}"
        )

    # ================= CEP =================
    def clean_cep(self):
        cep = self.cleaned_data.get('cep')

        if not cep:
            return cep

        numeros = re.sub(r'\D', '', cep)

        if len(numeros) != 8:
            raise forms.ValidationError("CEP inválido.")

        return f"{numeros[:5]}-{numeros[5:]}"

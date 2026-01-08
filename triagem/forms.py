from django import forms
from .models import Triagem


class TriagemForm(forms.ModelForm):
    """
    Formulário clínico de Triagem - Acolhimento com Classificação de Risco (SUS)
    """

    class Meta:
        model = Triagem
        exclude = [
            'atendimento',
            'enfermeiro',
            'data_hora_triagem',
        ]

        widgets = {

            # =========================
            # QUEIXA PRINCIPAL
            # =========================
            'queixa_principal': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3,
                    'placeholder': 'Descreva a queixa principal do paciente'
                }
            ),

            'inicio_sintomas': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ex: há 2 horas, ontem à noite'
                }
            ),

            # =========================
            # SINAIS VITAIS
            # =========================
            'pressao_arterial': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ex: 120/80'
                }
            ),

            'frequencia_cardiaca': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'min': 0
                }
            ),

            'frequencia_respiratoria': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'min': 0
                }
            ),

            'temperatura': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'step': '0.1'
                }
            ),

            'saturacao_oxigenio': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'min': 0,
                    'max': 100
                }
            ),

            'dor': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'min': 0,
                    'max': 10
                }
            ),

            # =========================
            # AVALIAÇÃO CLÍNICA
            # =========================
            'nivel_consciencia': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ex: Alerta, Sonolento, Confuso'
                }
            ),

            'mobilidade': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ex: Deambula, Acamado'
                }
            ),

            'sangramento': forms.CheckboxInput(
                attrs={'class': 'form-check-input'}
            ),

            'dispneia': forms.CheckboxInput(
                attrs={'class': 'form-check-input'}
            ),

            'dor_toracica': forms.CheckboxInput(
                attrs={'class': 'form-check-input'}
            ),

            'nausea_vomito': forms.CheckboxInput(
                attrs={'class': 'form-check-input'}
            ),

            # =========================
            # CLASSIFICAÇÃO DE RISCO
            # =========================
            'classificacao_risco': forms.Select(
                attrs={'class': 'form-select'}
            ),

            # =========================
            # CONDUTA / OBSERVAÇÕES
            # =========================
            'conduta': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3,
                    'placeholder': 'Conduta inicial / Encaminhamento'
                }
            ),

            'observacoes': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3
                }
            ),
        }

    # =========================
    # VALIDAÇÕES CLÍNICAS
    # =========================
    def clean_dor(self):
        dor = self.cleaned_data.get('dor')
        if dor is not None and dor > 10:
            raise forms.ValidationError('A escala de dor deve estar entre 0 e 10.')
        return dor

    def clean_pressao_arterial(self):
        pa = self.cleaned_data.get('pressao_arterial')
        if pa and '/' not in pa:
            raise forms.ValidationError('Formato inválido. Use o padrão 120/80.')
        return pa

    def clean_saturacao_oxigenio(self):
        sat = self.cleaned_data.get('saturacao_oxigenio')
        if sat is not None and (sat < 0 or sat > 100):
            raise forms.ValidationError('A saturação deve estar entre 0 e 100%.')
        return sat

from django import forms
from .models import Matricula
"""
class MatriculaForm(forms.ModelForm):
    class Meta:
        model = Matricula
        fields = ['nome_responsavel', 'nome_crianca', 'documento']"""
class MatriculaForm(forms.ModelForm):
    class Meta:
        model = Matricula
        fields = [
            'nome_crianca',
            'data_nascimento',
            'sexo',
            'nome_responsavel',
            'cpf_responsavel',
            'telefone',
            'email',
            'endereco_rua',
            'endereco_numero',
            'endereco_bairro',
            'endereco_cidade',
            'endereco_uf',
            'certidao_nascimento',
            'documento_responsavel',
            'comprovante_residencia',
        ]

        widgets = {
            'data_nascimento': forms.DateInput(
                format='%d/%m/%Y',
                attrs={
                    'class': 'form-control',
                    'placeholder': 'dd/mm/aaaa',
                    'type': 'text',  # Usa type text para permitir o formato brasileiro
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['data_nascimento'].input_formats = ['%d/%m/%Y']



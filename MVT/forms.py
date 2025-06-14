from django import forms
from .models import Matricula

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
        
        labels = {
            'nome_crianca': 'Nome da Criança',
            'data_nascimento': 'Data de Nascimento',
            'sexo': 'Sexo',
            'nome_responsavel': 'Nome do Responsável',
            'cpf_responsavel': 'CPF do Responsável',
            'telefone': 'Telefone',
            'email': 'E-mail',
            'endereco_rua': 'Rua',
            'endereco_numero': 'Número',
            'endereco_bairro': 'Bairro',
            'endereco_cidade': 'Cidade',
            'endereco_uf': 'UF',
            'certidao_nascimento': 'Certidão de Nascimento da Criança(upload)',
            'documento_responsavel': 'Documento do Responsável (upload)',
            'comprovante_residencia': 'Comprovante de Residência (upload)',
        }

        widgets = {
            'data_nascimento': forms.DateInput(
                format='%d/%m/%Y',
                attrs={
                    'class': 'form-control',
                    'placeholder': '01/01/1999',
                    'type': 'text',  
                }
            ),
            
            'cpf_responsavel': forms.TextInput(
                attrs={
                'class': 'form-control',
                'placeholder': '000.000.000-00',
                'type': 'text',
                'maxlength': '14',  
                }
             ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['data_nascimento'].input_formats = ['%d/%m/%Y']



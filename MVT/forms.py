from django import forms
from .models import Matricula

class MatriculaForm(forms.ModelForm):
    class Meta:
        model = Matricula
        fields = ['nome_responsavel', 'nome_crianca', 'documento']


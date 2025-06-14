from django.contrib import admin
from .models import RegiaoAdministrativa, Creche, Matricula
from .models import Matricula
from django import forms

admin.site.register(RegiaoAdministrativa)
admin.site.register(Creche)


class MatriculaAdminForm(forms.ModelForm):
    class Meta:
        model = Matricula
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.status != 'recusada':
            self.fields['motivo_recusa'].widget = forms.HiddenInput()

@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    form = MatriculaAdminForm
    list_display = ('id', 'nome_responsavel', 'status', 'motivo_recusa',)
    actions = ['aprovar_matricula', 'recusar_matricula']

    def aprovar_matricula(self, request, queryset):
        updated = queryset.update(status='aprovada', motivo_recusa='')
        self.message_user(request, f'{updated} matrículas aprovadas com sucesso.')
    aprovar_matricula.short_description = "Aprovar matrículas selecionadas"

    def recusar_matricula(self, request, queryset):
        updated = queryset.update(status='recusada', motivo_recusa='Dados inconsistentes ou Documentos Ilegíveis. Realizar uma nova matrícula.')
        self.message_user(request, f'{updated} Dados inconsistentes ou Documentos Ilegíveis. Realizar uma nova matrícula.')
    recusar_matricula.short_description = "Recusar matrículas selecionadas com motivo padrão"



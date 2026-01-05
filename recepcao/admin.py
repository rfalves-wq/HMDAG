from django.contrib import admin
from .models import Atendimento

@admin.register(Atendimento)
class AtendimentoAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'status', 'enfermeiro', 'data_hora_chegada')
    list_filter = ('status',)
    search_fields = ('paciente__nome_completo',)

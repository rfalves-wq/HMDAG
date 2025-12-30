
from django.views.generic import ListView
from  . import models

class PacienteListView(ListView):
    model = models.Paciente
    template_name = 'paciente_list.html'
    context_object_name = 'pacientes'

    def get_queryset(self):
        queryset = super().get_queryset()
        nome_completo = self.request.GET.get('nome_completo')

        if nome_completo:
            queryset = queryset.filter(nome_completo__icontains=nome_completo)

        return queryset
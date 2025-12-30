
from django.views.generic import ListView
from  . import models

class PacienteListView(ListView):
    model = models.Paciente
    template_name = 'paciente_list.html'
    context_object_name = 'pacientes'

    
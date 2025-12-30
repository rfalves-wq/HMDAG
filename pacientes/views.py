from django.urls import reverse_lazy 


from django.views.generic import ListView, CreateView, DetailView

from  . import models, forms
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
    
class PacienteCreateView(CreateView):
    model = models.Paciente
    template_name = 'paciente_create.html'
    form_class = forms.PacienteForm
    success_url = reverse_lazy('pacientes:list')
    

class PacienteDetailView(DetailView):
    model = models.Paciente
    template_name = 'paciente_detail.html'
    permission_required = 'pacientes:DetailView'
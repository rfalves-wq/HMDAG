from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
)
from .models import TecnicoEnfermagem
from .forms import TecnicoEnfermagemForm
class TecnicoEnfermagemListView(ListView):
    model = TecnicoEnfermagem
    template_name = 'tecnico_enfermagem/list.html'
    context_object_name = 'tecnicos'
    paginate_by = 10

    def get_queryset(self):
        queryset = TecnicoEnfermagem.objects.all()
        search = self.request.GET.get('search')

        if search:
            queryset = queryset.filter(
                nome_completo__icontains=search
            )

        return queryset
class TecnicoEnfermagemCreateView(CreateView):
    model = TecnicoEnfermagem
    form_class = TecnicoEnfermagemForm
    template_name = 'tecnico_enfermagem/form.html'
    success_url = reverse_lazy('tecnico_enfermagem_list')
class TecnicoEnfermagemUpdateView(UpdateView):
    model = TecnicoEnfermagem
    form_class = TecnicoEnfermagemForm
    template_name = 'tecnico_enfermagem/form.html'
    success_url = reverse_lazy('tecnico_enfermagem_list')
class TecnicoEnfermagemDetailView(DetailView):
    model = TecnicoEnfermagem
    template_name = 'tecnico_enfermagem/detail.html'
    context_object_name = 'tecnico'
class TecnicoEnfermagemDeleteView(DeleteView):
    model = TecnicoEnfermagem
    template_name = 'tecnico_enfermagem/confirm_delete.html'
    success_url = reverse_lazy('tecnico_enfermagem_list')

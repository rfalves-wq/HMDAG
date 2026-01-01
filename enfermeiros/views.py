from django.urls import reverse_lazy 


from django.views.generic import ListView, CreateView, DetailView,UpdateView,DeleteView

from  . import models, forms
class EnfermeiroListView(ListView):
    model = models.Enfermeiro
    template_name = 'enfermeiro_list.html'
    context_object_name = 'enfermeiros'

    def get_queryset(self):
        queryset = super().get_queryset()
        nome_completo = self.request.GET.get('nome_completo')
        cpf = self.request.GET.get('cpf')

        if nome_completo:
            queryset = queryset.filter(nome_completo__icontains=nome_completo)
        if cpf:
            queryset = queryset.filter(cpf__icontains=cpf)

        return queryset
    
class EnfermeiroCreateView(CreateView):
    model = models.Enfermeiro
    template_name = 'enfermeiro_create.html'
    form_class = forms.EnfermeiroForm
    success_url = reverse_lazy('enfermeiros:list')
    

class EnfermeiroDetailView(DetailView):
    model = models.Enfermeiro
    template_name = 'enfermeiro_detail.html'
    permission_required = 'enfermeiros:DetailView'


class EnfermeiroUpdateView(UpdateView):
    model = models.Enfermeiro
    template_name = 'enfermeiro_update.html'
    form_class = forms.EnfermeiroForm
    success_url = reverse_lazy('enfermeiros:list')
    


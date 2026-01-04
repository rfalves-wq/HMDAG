from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView
)
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Enfermeiro
from .forms import EnfermeiroForm

class EnfermeiroListView(LoginRequiredMixin, ListView):
    model = Enfermeiro
    template_name = 'enfermeiro_list.html'
    context_object_name = 'enfermeiros'
    paginate_by = 10

    def get_queryset(self):
        queryset = Enfermeiro.objects.filter(ativo=True).order_by('nome_completo')

        nome_completo = self.request.GET.get('nome_completo')
        

        if nome_completo:
            queryset = queryset.filter(
                nome_completo__icontains=nome_completo
            )

       

        return queryset


class EnfermeiroCreateView(LoginRequiredMixin, CreateView):
    model = Enfermeiro
    form_class = EnfermeiroForm
    template_name = 'enfermeiro_form.html'
    success_url = reverse_lazy('enfermeiro_list')

class EnfermeiroUpdateView(LoginRequiredMixin, UpdateView):
    model = Enfermeiro
    form_class = EnfermeiroForm
    template_name = 'enfermeiro_form.html'
    success_url = reverse_lazy('enfermeiro_list')

class EnfermeiroDetailView(LoginRequiredMixin, DetailView):
    model = Enfermeiro
    template_name = 'enfermeiro_detail.html'
    context_object_name = 'enfermeiro'

from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages


def enfermeiro_desativar(request, pk):
    enfermeiro = get_object_or_404(Enfermeiro, pk=pk)
    enfermeiro.ativo = False
    enfermeiro.save()

    messages.success(request, 'Enfermeiro desativado com sucesso.')
    return redirect('enfermeiro_list')

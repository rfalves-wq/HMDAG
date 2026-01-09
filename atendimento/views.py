from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import AtendimentoMedicoForm
from .models import AtendimentoMedico

def criar_atendimento(request):
    if request.method == 'POST':
        form = AtendimentoMedicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_atendimentos')
    else:
        form = AtendimentoMedicoForm()
    return render(request, 'atendimento/form.html', {'form': form})

def lista_atendimentos(request):
    atendimentos = AtendimentoMedico.objects.all()
    return render(request, 'atendimento/lista.html', {'atendimentos': atendimentos})

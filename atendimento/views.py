from django.shortcuts import render
from pacientes.models import Paciente
from triagem.models import Triagem
from .forms import AtendimentoMedicoForm

def criar_atendimento(request, paciente_id):
    paciente = Paciente.objects.get(id=paciente_id)

    # BUSCAR A ÚLTIMA TRIAGEM DO PACIENTE
    triagem = Triagem.objects.filter(
        paciente=paciente
    ).order_by('-data_hora').first()

    if request.method == 'POST':
        form = AtendimentoMedicoForm(request.POST)
        if form.is_valid():
            atendimento = form.save(commit=False)
            atendimento.paciente = paciente
            atendimento.save()
    else:
        form = AtendimentoMedicoForm()

    return render(request, 'atendimento/form.html', {
        'form': form,
        'paciente': paciente,
        'triagem': triagem
    })

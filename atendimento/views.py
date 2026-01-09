from django.shortcuts import render
from triagem.models import Triagem
from .forms import AtendimentoMedicoForm

def criar_atendimento(request):
    triagem = Triagem.objects.filter(
        status='aguardando_medico'
    ).order_by('-prioridade', 'data_hora').first()

    if not triagem:
        return render(request, 'atendimento/sem_paciente.html')

    paciente = triagem.paciente

    if request.method == 'POST':
        form = AtendimentoMedicoForm(request.POST)
        if form.is_valid():
            atendimento = form.save(commit=False)
            atendimento.paciente = paciente
            atendimento.triagem = triagem
            atendimento.save()

            # Finaliza a triagem após atendimento médico
            triagem.status = 'concluida'
            triagem.save()

    else:
        form = AtendimentoMedicoForm()

    return render(request, 'atendimento/form.html', {
        'form': form,
        'paciente': paciente,
        'triagem': triagem
    })


from django.utils import timezone

def fila_medica(request):
    triagens = Triagem.objects.filter(
        status='aguardando_medico'
    ).order_by('-prioridade', 'data_hora')

    return render(request, 'atendimento/fila_medica.html', {
        'triagens': triagens,
        'now': timezone.now()
    })


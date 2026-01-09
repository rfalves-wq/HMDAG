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

from django.shortcuts import render
from django.db.models import Case, When, IntegerField
from django.utils import timezone
from triagem.models import Triagem

def fila_medica(request):
    triagens = (
        Triagem.objects
        .filter(status='aguardando_medico')
        .annotate(
            prioridade_ordem=Case(
                When(prioridade='vermelho', then=0),
                When(prioridade='amarelo', then=1),
                When(prioridade='verde', then=2),
                When(prioridade='azul', then=3),
                output_field=IntegerField()
            )
        )
        .order_by('prioridade_ordem', 'data_hora')
    )

    return render(request, 'atendimento/fila_medica.html', {
        'triagens': triagens,
        'now': timezone.now()
    })


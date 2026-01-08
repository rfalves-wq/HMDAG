from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from recepcao.models import Atendimento
from .models import Triagem
from .forms import TriagemForm

#@login_required
def iniciar_triagem(request, atendimento_id):
    atendimento = get_object_or_404(
        Atendimento,
        id=atendimento_id,
        status='aguardando_triagem'
    )

    # Bloqueia o atendimento para outros enfermeiros
    atendimento.status = 'em_triagem'
    atendimento.save(update_fields=['status'])

    return redirect('concluir_triagem', atendimento_id=atendimento.id)

#@login_required
def concluir_triagem(request, atendimento_id):
    atendimento = get_object_or_404(
        Atendimento,
        id=atendimento_id,
        status='em_triagem'
    )

    # Evita triagem duplicada
    if hasattr(atendimento, 'triagem'):
        messages.warning(request, 'Este atendimento já possui triagem registrada.')
        return redirect('fila_triagem')

    if request.method == 'POST':
        form = TriagemForm(request.POST)
        if form.is_valid():
            triagem = form.save(commit=False)
            triagem.atendimento = atendimento
            triagem.enfermeiro = request.user.enfermeiro
            triagem.save()

            atendimento.status = 'triagem_concluida'
            atendimento.save(update_fields=['status'])

            messages.success(request, 'Triagem realizada com sucesso.')
            return redirect('fila_medica')
    else:
        form = TriagemForm()

    return render(
        request,
        'triagem/form.html',
        {
            'form': form,
            'atendimento': atendimento
        }
    )

from django.shortcuts import render
from recepcao.models import Atendimento


def fila_triagem(request):
    atendimentos = Atendimento.objects.filter(
        status='aguardando_triagem'
    ).select_related('paciente')

    return render(
        request,
        'triagem/fila.html',
        {
            'atendimentos': atendimentos
        }
    )

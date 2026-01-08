from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import AtendimentoForm
from .models import Atendimento

def atendimento_create(request):
   if request.method == 'POST':
       form = AtendimentoForm(request.POST)
       if form.is_valid():
           atendimento = form.save(commit=False)
           atendimento.status = 'aguardando_triagem'
           atendimento.save()
           return redirect('fila_triagem')
   else:
       form = AtendimentoForm()

    #return render(request, 'recepcao/atendimento_form.html', {'form': form})

def fila_triagem(request):
    atendimentos = Atendimento.objects.filter(
        status='aguardando_triagem'
    )
    return render(request, 'recepcao/fila_triagem.html', {
        'atendimentos': atendimentos
    })

from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .forms import AtendimentoForm
from .models import Atendimento
from pacientes.models import Paciente
from triagem.models import Triagem

def atendimento_create(request, paciente_id=None):
    pacientes = []
    paciente = None

    termo = request.GET.get('q')
    if termo:
        pacientes = Paciente.objects.filter(
            Q(nome_completo__icontains=termo) |
            Q(cpf__icontains=termo) |
            Q(cns__icontains=termo)
        )

    if paciente_id:
        paciente = get_object_or_404(Paciente, id=paciente_id)

    if request.method == 'POST' and paciente:
        form = AtendimentoForm(request.POST)
        if form.is_valid():
            # Salva o atendimento
            atendimento = form.save(commit=False)
            atendimento.paciente = paciente
            atendimento.status = 'aguardando_triagem'
            atendimento.save()

            # ✅ Cria a triagem automaticamente
            Triagem.objects.create(
                paciente=paciente,
                status='aguardando'
            )

            return redirect('fila_triagem')
    else:
        form = AtendimentoForm()

    return render(request, 'recepcao/atendimento_form.html', {
        'form': form,
        'pacientes': pacientes,
        'paciente': paciente
    })

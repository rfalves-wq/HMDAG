from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Triagem
from .forms import TriagemForm
from django.utils import timezone

def fila_triagem(request):
    triagens = Triagem.objects.filter(status='aguardando').order_by('data_hora')
    return render(request, 'triagem/fila_triagem.html', {'triagens': triagens})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Triagem
from .forms import TriagemForm

def triagem_atender(request, triagem_id):
    triagem = get_object_or_404(Triagem, id=triagem_id)

    if request.method == 'POST':
        form = TriagemForm(request.POST, instance=triagem)
        if form.is_valid():
            triagem = form.save(commit=False)
            triagem.status = 'concluida'
            
            # ✅ Associa o enfermeiro logado
            if hasattr(request.user, 'enfermeiro'):
                triagem.enfermeiro = request.user.enfermeiro
            else:
                # Opcional: se não tiver vinculado, deixa nulo ou mostra aviso
                triagem.enfermeiro = None

            triagem.save()
            return redirect('fila_triagem')
    else:
        # Atualiza status para 'em atendimento'
        triagem.status = 'em_atendimento'
        triagem.save()
        form = TriagemForm(instance=triagem)

    return render(request, 'triagem/triagem_atender.html', {
        'form': form,
        'triagem': triagem
    })
def fila_triagem(request):
    triagens = Triagem.objects.filter(status='aguardando').order_by(
        '-prioridade', 'data_hora'
    )
    return render(request, 'triagem/fila_triagem.html', {'triagens': triagens})

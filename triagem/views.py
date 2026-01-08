from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Triagem
from .forms import TriagemForm
from django.utils import timezone

def fila_triagem(request):
    triagens = Triagem.objects.filter(status='aguardando').order_by('data_hora')
    return render(request, 'triagem/fila_triagem.html', {'triagens': triagens})
def triagem_atender(request, triagem_id):
    triagem = get_object_or_404(Triagem, id=triagem_id)
    if request.method == 'POST':
        form = TriagemForm(request.POST, instance=triagem)
        if form.is_valid():
            triagem = form.save(commit=False)
            triagem.status = 'concluida'
            triagem.enfermeiro = request.user.enfermeiro  # assumindo que o usuário logado tem relação com enfermeiro
            triagem.save()
            return redirect('fila_triagem')
    else:
        triagem.status = 'em_atendimento'
        triagem.save()
        form = TriagemForm(instance=triagem)

    return render(request, 'triagem/triagem_atender.html', {'form': form, 'triagem': triagem})

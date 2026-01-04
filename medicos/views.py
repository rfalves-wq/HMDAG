from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q

from .models import Medico
from .forms import MedicoForm


def medico_list(request):
    medicos = Medico.objects.all().order_by('nome_completo')

    # BUSCA
    nome = request.GET.get('nome')
    cpf = request.GET.get('cpf')
    crm = request.GET.get('crm')
    especialidade = request.GET.get('especialidade')

    if nome:
        medicos = medicos.filter(nome_completo__icontains=nome)

    if cpf:
        medicos = medicos.filter(cpf__icontains=cpf)

    if crm:
        medicos = medicos.filter(crm__icontains=crm)

    if especialidade:
        medicos = medicos.filter(especialidade__icontains=especialidade)

    context = {
        'medicos': medicos
    }
    return render(request, 'medicos/medico_list.html', context)


def medico_create(request):
    if request.method == 'POST':
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Médico cadastrado com sucesso.')
            return redirect('medico_list')
    else:
        form = MedicoForm()

    return render(request, 'medicos/medico_form.html', {
        'form': form,
        'titulo': 'Cadastrar Médico'
    })


def medico_update(request, pk):
    medico = get_object_or_404(Medico, pk=pk)

    if request.method == 'POST':
        form = MedicoForm(request.POST, instance=medico)
        if form.is_valid():
            form.save()
            messages.success(request, 'Médico atualizado com sucesso.')
            return redirect('medico_list')
    else:
        form = MedicoForm(instance=medico)

    return render(request, 'medicos/medico_form.html', {
        'form': form,
        'titulo': 'Editar Médico'
    })


def medico_delete(request, pk):
    medico = get_object_or_404(Medico, pk=pk)

    if request.method == 'POST':
        medico.delete()
        messages.success(request, 'Médico excluído com sucesso.')
        return redirect('medico_list')

    return render(request, 'medicos/medico_confirm_delete.html', {
        'medico': medico
    })

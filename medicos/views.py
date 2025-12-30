from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Medico
from .forms import MedicoForm


def medico_list(request):
    medicos = Medico.objects.filter(ativo=True).order_by('nome_completo')
    return render(
        request,
        'medicos/medico_list.html',
        {'medicos': medicos}
    )


def medico_create(request):
    form = MedicoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('medicos:lista')

    return render(
        request,
        'medicos/medico_form.html',
        {'form': form}
    )


def medico_update(request, pk):
    medico = get_object_or_404(Medico, pk=pk)
    form = MedicoForm(request.POST or None, instance=medico)

    if form.is_valid():
        form.save()
        return redirect('medicos:lista')

    return render(
        request,
        'medicos/medico_form.html',
        {'form': form, 'medico': medico}
    )


def medico_delete(request, pk):
    medico = get_object_or_404(Medico, pk=pk)

    if request.method == 'POST':
        medico.ativo = False  # exclusão lógica (padrão SUS)
        medico.save()
        return redirect('medicos:lista')

    return render(
        request,
        'medicos/medico_confirm_delete.html',
        {'medico': medico}
    )

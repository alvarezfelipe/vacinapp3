from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator

from .models import *
from .forms import *

# Create your views here.
def criar_vacinacao(request):
    model = CadastroVacinal
    form = VacinacaoForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            vacinacao = form.save()
            return redirect('/vacinacao/visualizar_vacinacao/' + str(vacinacao.id))
    return render(request, 'vacinacao/cadastrar_vacinacao.html', {'form':form})

def listar_vacinacao(request):
    busca = request.GET.get('busca')
    if busca:
        vacinacao_list = CadastroVacinal.objects.filter(
            paciente__icontains=busca).order_by('paciente')
    else:
        vacinacao_list = CadastroVacinal.objects.all().order_by('paciente')
    paginacao = Paginator(vacinacao_list, 10)
    pagina = request.GET.get('page')
    vacinacao = paginacao.get_page(pagina)
    context = {
        'vacinacao':vacinacao
    }

    return render(request, 'vacinacao/listar_vacinacao.html', context)

def editar_vacinacao(request, id):
    vacinacao = get_object_or_404(CadastroVacinal, pk = id)
    form = VacinacaoForm(request.POST or None, instance = vacinacao)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.save()
            return render(request, 'vacinacao/visualizar_vacinacao.html', {'vacinacao':vacinacao})
    
    context = {
        'form': form,
        'vacinacao':vacinacao,
    }

    return render(request, 'vacinacao/editar_vacinacao.html', context)

def visualizar_vacinacao(request, id):
    vacinacao = get_object_or_404(CadastroVacinal, id = id)
    context = {
        'vacinacao': vacinacao
    }
    return render(request, 'vacinacao/visualizar_vacinacao.html', context)
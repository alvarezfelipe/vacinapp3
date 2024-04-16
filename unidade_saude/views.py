from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages

from .models import *
from .forms import *

# Views para CRUD de Unidades de Saúde.
def criar_unidade(request):
    model = UnidadeSaude
    form = UnidadeForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            unidade_saude = form.save()
            return redirect('/unidade/visualizar_unidade/' + str(unidade_saude.id))
        else:
            messages.error('Erro ao cadastrar. Contate o administrador.')
    return render(request, 'unidade/cadastrar_unidade.html', {'form':form})

def listar_unidade(request):
    busca = request.GET.get('busca')
    if busca:
        unidades_list = UnidadeSaude.objects.filter(
            uni_nome__icontains=busca).order_by('uni_nome')
    else:
        unidades_list = UnidadeSaude.objects.all().order_by('uni_nome')
    paginacao = Paginator(unidades_list, 10)
    pagina = request.GET.get('page')
    unidades = paginacao.get_page(pagina)
    context = {
        'unidades': unidades
    }

    return render(request, 'unidade/listar_unidades.html', context)

def editar_unidade(request, id):
    unidade = get_object_or_404(UnidadeSaude, pk = id)
    form = UnidadeForm(request.POST or None, instance = unidade)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Alterado com sucesso!')
            return render(request, 'unidade/visualizar_unidade.html', {'unidade':unidade})
        else:
            messages.error(request, 'Erro ao editar. Contate o administrador.')

    context = {
        'form':form,
        'unidade':unidade,
    }

    return render(request, 'unidade/editar_unidade.html', context)

def visualizar_unidade(request, id):
    unidade = get_object_or_404(UnidadeSaude, id = id)
    context = {
        'unidade': unidade
    }
    return render(request, 'unidade/visualizar_unidade.html', context)

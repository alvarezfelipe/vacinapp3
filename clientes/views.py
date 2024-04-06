from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator

from .forms import *
from .models import *

# Create your views here.
def criar_crianca(request):
    model = Crianca
    form = CadastroCriancaForm(request.POST or None)

    if str(request.method) == "POST":
        if form.is_valid():
            crianca = form.save()
            messages.success(request, 'Criança cadastrada com sucesso')
            # return redirect('visualizar_crianca', crianca.pk)
            # return render(request, 'crianca/visualizar_crianca.html', {'crianca': form.cleaned_data})
    return render(request, 'crianca/cadastrar_crianca.html', {'form':form})

def listar_crianca(request):
    busca = request.GET.get('busca')
    if busca:
        criancas_list = Crianca.objects.filter(
            crianca_nome__icontains=busca).order_by('crianca_nome')
    else:
        criancas_list = Crianca.objects.all().order_by('crianca_nome')
    paginacao = Paginator(criancas_list, 10)
    pagina = request.GET.get('page')
    criancas = paginacao.get_page(pagina)
    context = {
        'criancas':criancas
    }
    return render(request, 'crianca/listar_criancas.html', context)

def editar_crianca(request, id):
    crianca = get_object_or_404(Crianca, pk = id)
    form = CadastroCriancaForm(request.POST or None, instance=crianca)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Criança atualizada com sucesso!')
            return render(request, 'crianca/visualizar_crianca.html', {'crianca':crianca})
        else:
            messages.error(request, 'Erro ao editar. Tente novamente.')
    
    context = {
        'form':form,
        'crianca':crianca
    }
    return render(request, 'crianca/editar_crianca.html', context)

def visualizar_crianca(request, id):
    crianca = get_object_or_404(Crianca, pk=id)
    context = {
        'crianca': crianca
    }
    return render(request, 'crianca/visualizar_crianca.html', context)

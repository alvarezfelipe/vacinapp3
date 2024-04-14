from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator

from .forms import *
from .models import *

# Views para crianças
def criar_crianca(request):
    model = Crianca
    form = CadastroCriancaForm(request.POST or None)

    if str(request.method) == "POST":
        if form.is_valid():
            crianca = form.save()
            return redirect('/crianca/visualizar_crianca/' + str(crianca.id))          
        
        else:
            messages.error(request, 'Erro ao cadastrar. Contate o administrador.')
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

def teste(request):
    return render(request, 'crianca/hello.html')

# Views para pais/responsáveis
def criar_resp(request):
    model = Pais
    form = CadastroPaiForm(request.POST or None)

    if str(request.method) == "POST":
        if form.is_valid():
            pai = form.save()
            return redirect('/responsavel/visualizar_resp/' + str(pai.id))          
        
        else:
            messages.error(request, 'Erro ao cadastrar. Contate o administrador.')
    return render(request, 'responsavel/cadastrar_resp.html', {'form':form})

def listar_resp(request):
    busca = request.GET.get('busca')
    if busca:
        pais_list = Pais.objects.filter(
            pai_nome__icontains=busca).order_by('pai_nome')
    else:
        pais_list = Pais.objects.all().order_by('pai_nome')
    paginacao = Paginator(pais_list, 10)
    pagina = request.GET.get('page')
    pais = paginacao.get_page(pagina)
    context = {
        'pais':pais
    }
    return render(request, 'responsavel/listar_resp.html', context)

def editar_resp(request, id):
    pai = get_object_or_404(Pais, pk = id)
    form = CadastroPaiForm(request.POST or None, instance=pai)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Responsável atualizado com sucesso!')
            return render(request, 'responsavel/visualizar_resp.html', {'pais':pai})
        else:
            messages.error(request, 'Erro ao editar. Tente novamente.')
    
    context = {
        'form':form,
        'pais':pai,
    }
    return render(request, 'responsavel/editar_resp.html', context)

def visualizar_resp(request, id):
    pai = get_object_or_404(Pais, pk=id)
    context = {
        'pais': pai
    }
    return render(request, 'responsavel/visualizar_resp.html', context)

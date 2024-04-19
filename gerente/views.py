from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator

from .forms import *
from .models import *

# Views para crianças
def criar_gerente(request):
    model = Gerente
    form = GerenteForm(request.POST or None)

    if str(request.method) == "POST":
        if form.is_valid():
            gerente = form.save()
            return redirect('/gerente/visualizar_gerente/' + str(gerente.id))          
        
        else:
            messages.error(request, 'Erro ao cadastrar. Contate o administrador.')
    return render(request, 'gerente/cadastrar_gerente.html', {'form':form})

def listar_gerente(request):
    busca = request.GET.get('busca')
    if busca:
        gerentes_list = Gerente.objects.filter(
            gerente_nome__icontains=busca).order_by('gerente_nome')
    else:
        gerentes_list = Gerente.objects.all().order_by('gerente_nome')
    paginacao = Paginator(gerentes_list, 10)
    pagina = request.GET.get('page')
    gerentes = paginacao.get_page(pagina)
    context = {
        'gerentes':gerentes
    }
    return render(request, 'gerente/listar_gerente.html', context)

def editar_gerente(request, id):
    gerente = get_object_or_404(Gerente, pk = id)
    form = GerenteForm(request.POST or None, instance=gerente)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.save()            
            return render(request, 'gerente/visualizar_gerente.html', {'gerente':gerente})
        else:
            messages.error(request, 'Erro ao editar. Tente novamente.')
    
    context = {
        'form':form,
        'gerente':gerente
    }
    return render(request, 'gerente/editar_gerente.html', context)

def visualizar_gerente(request, id):
    gerente = get_object_or_404(Gerente, pk=id)
    context = {
        'gerente':gerente
    }
    return render(request, 'gerente/visualizar_gerente.html', context)
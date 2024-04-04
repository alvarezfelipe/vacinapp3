from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator

from .forms import *
from .models import *

# Create your views here.
def criar_vacina(request):
    model = Vacina
    form = VacinaForm(request.POST or None)

    if str(request.method) == "POST":
        if form.is_valid():
            vacina = form.save()
            messages.success(request, 'Vacina cadastrada com sucesso')
            return redirect('hello')
    return render(request, 'vacina/vacinahome.html', {'form':form})

def teste(request):
    return render(request, 'vacina/hello.html')

def listar_vacinas(request):
    busca = request.GET.get('busca')
    if busca:
        vacinas_list = Vacina.objects.filter(
            vacina_nome__icontains=busca).order_by('vacina_nome')
    else:
        vacinas_list = Vacina.objects.all().order_by('vacina_nome')
    paginacao = Paginator(vacinas_list, 10)
    pagina = request.GET.get('page')    
    vacinas = paginacao.get_page(pagina)
    context = {
        'vacinas': vacinas
    }
    return render(request, 'vacina/listar_vacinas.html', context)

def editar_vacina(request, id):
    vacina = get_object_or_404(Vacina, pk=id)
    form = VacinaForm(request.POST or None, instance=vacina)
    if str(request.method) =='POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Vacina atualizada com sucesso!')
            return render(request, 'vacina/visualizar_vacina.html', {'vacina':vacina})
        else:
            messages.error(request, 'Erro ao editar a vacina. Tente novamente.')
    context = {
        'form': form,
        'vacina': vacina
    }
    return render(request, 'vacina/editar_vacina.html', context)

def visualizar_vacina(request, id):
    vacina = get_object_or_404(Vacina, pk=id)
    context = {
        'vacina': vacina
    }
    return render(request, 'vacina/visualizar_vacina.html', context)
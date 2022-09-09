from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from .forms import MovimentacaoFomr
from .models import Movimentacao

# Create your views here.


def lista_movimentacoes(request):
    template_name = 'movimentacoes/lista_movimentacoes.html'
    movimentacoes = Movimentacao.objects.filter(usuario=request.user)
    context = {
        'movimentacoes': movimentacoes
    }
    return render(request, template_name, context)


def nova_movimentacao(request):
    template_name = 'movimentacoes/nova_movimentacao.html'
    context = {}
    if request.method == 'POST':
        form = MovimentacaoFomr(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.usuario = request.user
            f.save()
            messages.success(request, 'Movimentação salva com sucesso')
            return redirect('movimentacoes:lista_movimentacoes')
        else:
            form = MovimentacaoFomr(request.POST)
            context['form'] = form
    else:
        form = MovimentacaoFomr()
    context['form'] = form
    return render(request, template_name, context)

def editar_movimentacao(request, pk):
    template_name = 'movimentacoes/nova_movimentacao.html'
    context = {}
    movimentacao = get_object_or_404(Movimentacao, pk=pk)
    if request.method == 'POST':
        form = MovimentacaoFomr(data=request.POST, instance=movimentacao)
        if form.is_valid():
            form.save()
            messages.success(request, 'Movimentação alterada com sucesso.')
            return redirect('movimentacoes:lista_movimentacoes')
        else:
            form = MovimentacaoFomr(instance=movimentacao)
            context['form'] = form
    else:
        form = MovimentacaoFomr(instance=movimentacao)
    context['form'] = form
    return render(request, template_name, context)

def apagar_movimentacao(request, pk):
    movimentacao = get_object_or_404(Movimentacao, pk=pk)
    movimentacao.delete()
    return redirect('movimentacoes:lista_movimentacoes')
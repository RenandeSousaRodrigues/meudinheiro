from django.shortcuts import render, redirect

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
    template_name = 'movimentacoes/nova_movimentacoes.html'
    context = {}
    if request.method == 'POST':
        form = MovimentacaoFomr(request.POST)
        if forms.is_valid():
            f = form.save(commit=False)
            f.usuario = request.user
            f.save()
            from django.contrib import messages
            messages.sucess(request, 'Movimentação salva com sucesso')
            return redirect('movimentacoes:lista_movimentacoes')
        else:
            form = MovimentacaoFomr(request.POST)
            context['fora'] = form
    else:
        form = MovimentacaoFomr()
    context['fora'] = form
    return render(request, template_name, context)
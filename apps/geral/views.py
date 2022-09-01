from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import CategoriaForm


# Create your views here.
def principal(request):
    template_name = 'base.html'
    return render(request, template_name, {})


def nova_categoria(request):
    template_name = 'geral/nova_categoria.html' #nome do html que vai ser exibido
    context = {}
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.usuario = request.user
            f.save()
            messages.success(request, 'Categoria adicionada com sucesso.')
            return redirect('geral:lista_categorias')
        else:
            form = CategoriaForm(request.POST)
            context['form'] = form
    else:
        form = CategoriaForm()
    context['form'] = form
    return render(request, template_name, context)
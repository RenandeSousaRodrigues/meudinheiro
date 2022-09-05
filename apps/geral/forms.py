from django import forms

from .models import Categoria


class CategoriaForm(forms.ModelForm):
    # nome = forms.CharField(label='Nome', widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Categoria
        #fields = ['nome', 'descricao', 'tipo'] #lista quem vai mostrar
        #fields = '__all__' mostra todos
        exclude = ['usuario'] #exclui apenas o usuário
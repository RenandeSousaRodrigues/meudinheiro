from django import forms
from django.contrib.auth.models import User

from .models import Categoria


class CategoriaForm(forms.ModelForm):
    # nome = forms.CharField(label='Nome', widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Categoria
        #fields = ['nome', 'descricao', 'tipo'] #lista quem vai mostrar
        #fields = '__all__' mostra todos
        exclude = ['usuario'] #exclui apenas o usuário


class LoginForms(forms.Form):
    username = forms.CharField(label='Usuário', required=True)
    password = forms.CharField(label='Senha', required=True, widget=forms.PasswordInput())


class UserForm(forms.ModelForm):


    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
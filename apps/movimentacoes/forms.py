from django import forms

from geral.models import Categoria
from .models import Movimentacao


class MovimentacaoFomr(forms.ModelForm):

    class Meta:
        model = Movimentacao
        exclude = ['usuario']


    def __int__(self, usuario, *args, **kwargs):
        super(MovimentacaoFomr, self).__init__(*args, **kwargs)
        self.fields['categoria'].queryset = Categoria.objects.filter(usuario=usuario)

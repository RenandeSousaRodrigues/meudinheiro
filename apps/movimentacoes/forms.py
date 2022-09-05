from django import forms

from .models import Movimentacao


class MovimentacaoFomr(forms.ModelForm):

    class Meta:
        model = Movimentacao
        exclude = ['usuario']
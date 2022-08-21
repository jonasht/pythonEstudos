from socket import fromshare
from django import forms

from .models import Produto

class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        # para pegar todos
        # fields = '__all__' 
        
        # outro jeito com dicionario
        fields = ['nome', 'preco', 'estoque', 'imagem']
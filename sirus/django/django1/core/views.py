from urllib import request
from django.shortcuts import render, HttpResponse
from .models import Produto
# Create your views here.

def index(request):
    produtos = Produto.objects.all().order_by('-id')

    context = {
        'meu_titulo': 'lista de produtos',
        'produtos': produtos
    }
    return render(request, 'index.html', context)


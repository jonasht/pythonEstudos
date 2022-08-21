from email import message
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from .models import Produto
from .forms import ProdutoModelForm
# Create your views here.

def index(request):
    produtos = Produto.objects.all().order_by('-id')

    context = {
        'meu_titulo': 'lista de produtos',
        'produtos': produtos
    }
    return render(request, 'index.html', context)

def produto(request):
    if request.method == 'POST':
        form = ProdutoModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto salvo com sucesso')
            form = ProdutoModelForm()
        else:
            messages.error(request, 'erro ao salvar o produto')    
    else:
        form = ProdutoModelForm()
    context = {'form': form}

    return render(request, 'produto.html', context)


def produto_submit(request):
    if request.method == 'POST':
        form = ProdutoModelForm(request.POST, request.FILES)
        if form.is_invalid():
            form.save()
            return redirect('index')
        else:
            messages.error(request, 'erro ao salvar o produto')
            return render(request, 'produto.html')
    else:
        return redirect('index')

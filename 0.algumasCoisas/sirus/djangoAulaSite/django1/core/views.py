from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate


from .models import Produto
from .forms import ProdutoModelForm
# Create your views here.

def login_user(request):
    # se ja estiver logado, nao fazer login de novo
    if request.user.is_authenticated:
        return redirect('/')
    
    return render(request, 'login.html')

def login_submit(request):
    if request.method == 'POST':
        if request.POST:
            usuario = request.POST.get('usuario')
            senha = request.POST.get('senha')
            user = authenticate(username=usuario, password=senha)

            if user:
                messages.success(request, 'login feito com sucesso')
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'error: usuario ou senha invalidos')
                return render(request, 'login.html')
                
    messages.error(request, 'erro ao logar, nao envio de dados')

    return render(request, 'login.html')


    
def index(request):
    print('=-'*49)
    print(dir(request.user))
    print(request.user.username)
    print('=-'*49)
    
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

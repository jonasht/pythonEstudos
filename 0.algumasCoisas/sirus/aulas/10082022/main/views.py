from django.shortcuts import render
from .forms import formUsuario

# Create your views here.

def criarUsuario(request):
    form = formUsuario(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            
        
    return render(request, 'main/form.html', {'form': form})



from django.shortcuts import render

# Create your views here.
from core.forms import PerfilForm
def index_request(request):
    if request.method == 'GET':
        form = PerfilForm()
        context = {
            'form': form
        }
        return render(request, 'index.html', context=context)
    else:
        form = PerfilForm(request.POST)
        
        if form.is_valid():
            perfil = form.save()
            form = PerfilForm()
  
            context = {
                'form': form
            }
            return render(request, 'index.html', context=context)
from django.urls import path
from .views import criarUsuario

urlpatterns = [
    path('', criarUsuario, name='cadastro')
    
]
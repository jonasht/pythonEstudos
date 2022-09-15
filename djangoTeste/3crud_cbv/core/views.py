from django.shortcuts import render
from django.views.generic import ListView
from core.models import Cliente

# Create your views here.
class ClienteList(ListView):
    model = Cliente
    queryset = Cliente.objects.all()
    
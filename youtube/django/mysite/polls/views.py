from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    return HttpResponse('<b>oi, este é meu primeiro site em</b> django')


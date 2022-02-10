from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.


def index(request):
    # return HttpResponse('<b>oi, este é meu primeiro site em</b> django')
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)



# def detail(request, question_id):
#     return HttpResponse(f'esta eh a pergunta de numero {question_id}')


def results(request, question_id):
    # return HttpResponse(f'esses sao os resultados da pergunta de numero{question_id}')
    question = Question(pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
    

def vote(request, question_id):
    return HttpResponse(f'voce estah votando na questao numero {question_id}')



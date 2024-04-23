from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import OracleQuestion
from .models import OracleAnswer

def index(request):
    latest_question_list = OracleQuestion.objects.order_by('category')
    context = {'latest_question_list': latest_question_list}
    return render(request, 'oracles/index.html', context)

def detail(request, question_id):
    question = OracleQuestion.objects.get(pk=question_id)
    return render(request, 'oracles/detail.html', {'question': question})

def category(request, category):
    latest_question_list = OracleQuestion.objects.filter(category=category)
    context = {'latest_question_list': latest_question_list}
    return render(request, 'oracles/category.html', context)
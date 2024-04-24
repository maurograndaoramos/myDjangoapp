from django.shortcuts import render
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
    questions = OracleQuestion.objects.filter(category=category)
    context = {
        'category': category,
        'questions': questions,
    }
    return render(request, 'oracles/category.html', context)

def indexCategory(request):
    categories = OracleQuestion.objects.order_by('category').values('category').distinct()
    context = {'categories': categories}
    return render(request, 'oracles/index-category.html', context)
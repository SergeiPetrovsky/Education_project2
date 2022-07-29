from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

def index(request):
    task = Task.objects.order_by("-created_on")
    parameters = {'title': 'Главная страница',
                  'tasks': task
                  }
    return render(request, 'index.html', parameters)

def about(request):
    return render(request, 'about.html')

def page1(request):
    return render(request, 'page1.html')

def page2(request):
    return render(request, 'page2.html')

def page3(request):
    return render(request, 'page3.html')

def create(request):
    return render(request, 'create.html')

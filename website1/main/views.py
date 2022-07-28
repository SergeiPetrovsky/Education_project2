from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

def index(request):
    task = Task.objects.all()
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

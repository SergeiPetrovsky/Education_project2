from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

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
    error = ''
    form = TaskForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')

        else:
            error = 'Форма заполнена неверно'

    context = {
        'form': form,
        'error': error
    }
    return render(request, 'create.html', context)

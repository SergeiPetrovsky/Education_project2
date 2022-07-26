from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Блок занятий №30</h1> <br> '
                        '<h2>Домашнее задание №1</h2><br> '
                        '<h1>Вывод произвольного текста</h1>')


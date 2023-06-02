from django.shortcuts import render
from django.http import HttpResponse


# Главная страница
def index(request):
    return HttpResponse('Главная страница')


# Страница со списком мороженого
def about(request):
    return HttpResponse('О проекте')

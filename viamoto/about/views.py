from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView


def index(request):
    return HttpResponse('Главная страница')


def about(request):
    return HttpResponse('О проекте')


class AboutTechView(TemplateView):
    template_name = 'about/tech.html'
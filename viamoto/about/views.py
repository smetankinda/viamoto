from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView


def index(request):
    context = {
        'post': 'post'
    }
    return render(request, 'about/index.html', context)


def about(request):
    return HttpResponse('О проекте')


class AboutTechView(TemplateView):
    template_name = 'about/tech.html'

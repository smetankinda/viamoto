from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView


class index(TemplateView):
    template_name = 'about/index.html'


class about(TemplateView):
    template_name = 'about/about.html'


def profile(request, username):
    # Здесь код запроса к модели и создание словаря контекста
    context = {
    }
    return render(request, 'users/profile.html', context)

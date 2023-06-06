from django.urls import path

from . import views

app_name = 'about'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about),
    path('tech/', views.AboutTechView.as_view(), name='tech'),
]

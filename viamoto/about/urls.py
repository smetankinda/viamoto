from django.urls import path

from . import views

app_name = 'about'

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('about/', views.about.as_view(), name='about'),
    path('profile/<str:username>/', views.profile, name='profile'),
]

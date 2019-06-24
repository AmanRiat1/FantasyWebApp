from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #pk is the content 
    path('', views.process, name='totalGames')
]
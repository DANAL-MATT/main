"""GNsys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path as url
from GotchaSys import views

urlpatterns = [
    path('', views.MainPage, name='mainpage'),
    path('secondpage', views.SecondPage),
    path('calculator', views.CalPage),
    path('games', views.GamesPage, name='games'),
    url(r'^gamepage/(\d+)$', views.IndGame, name='gamepage'),
    url(r'^gamepage/(\d+)/edit$', views.UpGame, name='updategame'),
    url(r'^gamepage/(\d+)/delete$', views.DelGame, name='deletegame'),
    url(r'^gamepage/(\d+)/storylines$', views.StoryPage, name='storylines'),
    url(r'^gamepage/(\d+)/storylines/delete$', views.DelStory, name='storydelete'),
    url(r'^gamepage/(\d+)/characters$', views.CharsPage, name='characters'),
    url(r'^gamepage/(\d+)/characters/view$', views.IndChar, name='characterview'),
    url(r'^gamepage/(\d+)/characters/delete$', views.DelChar, name='chardelete'),
    url(r'^gamepage/(\d+)/banners$', views.GachaPage, name='gachabanners'),
    url(r'^gamepage/(\d+)/banners/delete$', views.DelGacha, name='gachadelete'),
    url('admin/', admin.site.urls),
]

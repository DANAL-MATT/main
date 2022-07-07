from django.shortcuts import render, redirect
from django.http import HttpResponse
from GotchaSys.models import *

def MainPage(request):
    if request.method == 'POST':
        Feedback.objects.create(name=request.POST['user_name'],
            email=request.POST['user_email'],
            number=request.POST['user_number'],
            query=request.POST['user_query'])
        return redirect('/')
    samplename = Feedback.objects.all()
    return render(request, 'mainpage.html', {'forstoring': samplename})
    # return render(request, 'mainpage.html')

    # return render(request, 'mainpage.html', {'postName': request.POST.get('user_name'), 'postEmail': request.POST.get('user_email'), 'postNumber': request.POST.get('user_number'), 'postQuery': request.POST.get('user_query')})

def SecondPage(request):
    samplename = Feedback.objects.all()
    return render(request, 'secondpage.html', {'forstoring': samplename})

def CalPage(request):
    return render(request, 'gachacalculator.html')

def GamesPage(request):
    if request.method == 'POST':
        Games.objects.create(Game_Name=request.POST['game_name'],
            Genre=request.POST['game_genre'],
            Release_Date=request.POST['game_reldate'],
            Game_Description=request.POST['game_description'])
        return redirect('/games')
    gamestorage = Games.objects.all()
    return render(request, 'game.html', {'gamewareh': gamestorage})

def IndGame(request, gameID):
    specificgame = Games.objects.filter(Game_ID=gameID)
    return render(request, 'gamepage.html', {'specificgame': specificgame})

# Create your views here.

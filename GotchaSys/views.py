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

def UpGame(request, gameID):
    specificgame = Games.objects.get(Game_ID=gameID)
    specificgame.Game_Name = request.POST['game_editname']
    specificgame.Genre = request.POST['game_editgenre']
    specificgame.Release_Date = request.POST['game_editreldate']
    specificgame.Game_Description = request.POST['game_editdescription']
    specificgame.save()
    return redirect('/games')
    return render(request, 'game.html', {'specificgame': specificgame})

def DelGame(request, gameID):
    gametodelete = Games.objects.get(Game_ID=gameID)
    gametodelete.delete()
    return redirect('/games')
    return render(request, 'game.html', {'gametodelete':gametodelete})

def StoryPage(request, gameID):
    if request.method == 'POST':
        Storylines.objects.create(Chapter_Name=request.POST['story_name'],
            Chapter_Description=request.POST['story_desc'],
            Chapter_Setting=request.POST['story_setting'],
            Story_GameID=Games.objects.get(Game_ID=gameID))
        # return redirect('/gamepage')
    storystorage = Storylines.objects.all()
    return render(request, 'storylines.html', {'stories': storystorage})

# def UpStory(request, storyID):
#     storynum = Storylines.objects.get(Chapter_ID=storyID)
#     storynum.Chapter_Name = request.POST['game_editname']
#     storynum.Chapter_Description = request.POST['game_editgenre']
#     storynum.Chapter_Setting = request.POST['game_editreldate']
#     storynum.save()
#     return redirect()
#     return render(request, 'storylines.html', {'storynum': storynum})

def DelStory(request, storyID):
    storydelete = Storylines.objects.get(Chapter_ID=storyID)
    storydelete.delete()
    return redirect('/games')
    return render(request, 'storylines.html', {'storydelete':storydelete})

def CharsPage(request):
    if request.method == 'POST':
        Characters.objects.create(Character_Name=request.POST['char_name'],
            Character_Rarity=request.POST['char_rarity'],
            Char_Description=request.POST['char_desc'],
            Char_GameID=Games.objects.get(Game_ID=gameID))
        return redirect('/games')
    gamestorage = Games.objects.all()
    return render(request, 'gamespage.html', {'gamewareh': gamestorage})

# Create your views here.

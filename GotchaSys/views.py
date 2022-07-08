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

def DelFeed(request):
    deletefeed = Feedback.objects.all()
    deletefeed.delete()
    return redirect('/')
    return render(request, 'mainpage.html', {'deletefeed':deletefeed})

# def SecondPage(request):
#     samplename = Feedback.objects.all()
#     return render(request, 'secondpage.html', {'forstoring': samplename})

# def CalPage(request):
#     return render(request, 'gachacalculator.html')

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

def ViewStory(request):
    storyviews = Storylines.objects.all()
    return render(request, 'storylines.html', {'storyviews':storyviews})

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

def CharsPage(request, gameID):
    if request.method == 'POST':
        Characters.objects.create(Character_Name=request.POST['char_name'],
            Character_Rarity=request.POST['char_rarity'],
            Char_Description=request.POST['char_desc'],
            Char_GameID=Games.objects.get(Game_ID=gameID))
        # return redirect('/games')
    characterstorage = Characters.objects.all()
    return render(request, 'characters.html', {'charstore': characterstorage})

def IndChar(request, charID):
    charselect = Characters.objects.filter(Character_ID=charID)
    return render(request, 'characters.html', {'charselect': charselect})

def DelChar(request, charID):
    chardelete = Characters.objects.get(Character_ID=charID)
    chardelete.delete()
    return redirect('/games')
    return render(request, 'characters.html', {'chardelete':chardelete})

def ViewChars(request):
    charviews = Characters.objects.all()
    return render(request, 'characters.html', {'charviews':charviews})

def GachaPage(request, gameID):
    if request.method == 'POST':
        Gacha.objects.create(Banner_Name=request.POST['banner_name'],
            Banner_Type=request.POST['banner_type'],
            Banner_Description=request.POST['gacha_desc'],
            Banner_ReleaseDate=request.POST['gacha_reldate'],
            Banner_EndDate=request.POST['gacha_enddate'],
            Gacha_GameID=Games.objects.get(Game_ID=gameID))
        # return redirect('/games')
    gachastorage = Gacha.objects.all()
    return render(request, 'gachabanners.html', {'gachas': gachastorage})

def DelGacha(request, gachaID):
    gachadelete = Gacha.objects.get(Banner_ID=gachaID)
    gachadelete.delete()
    return redirect('/games')
    return render(request, 'gachabanners.html', {'gachadelete':gachadelete})

# Create your views here.

from django.shortcuts import render, redirect
from django.http import HttpResponse
from GotchaSys.models import Item

def MainPage(request):
    if request.method == 'POST':
        Item.objects.create(name=request.POST['user_name'],
            email=request.POST['user_email'],
            number=request.POST['user_number'],
            query=request.POST['user_query'])
        return redirect('/')
    samplename = Item.objects.all()
    return render(request, 'mainpage.html', {'forstoring': samplename})

    # return render(request, 'mainpage.html', {'postName': request.POST.get('user_name'), 'postEmail': request.POST.get('user_email'), 'postNumber': request.POST.get('user_number'), 'postQuery': request.POST.get('user_query')})
# Create your views here.

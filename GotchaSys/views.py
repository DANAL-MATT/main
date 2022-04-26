from django.shortcuts import render
from django.http import HttpResponse

def MainPage(request):
    return render(request, 'mainpage.html', {'postName': request.POST.get('user_name'), 'postEmail': request.POST.get('user_email'), 'postNumber': request.POST.get('user_number'), 'postQuery': request.POST.get('user_query')})
# Create your views here.

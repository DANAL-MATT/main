from django.shortcuts import render
from django.http import HttpResponse
from GotchaSys.models import Item

def MainPage(request):
	item1 = Item()
	item1.text1 = request.POST.get('postName', 'test')
	item1.save()

	return render(request, 'mainpage.html', {'postName': item1.text1,})
# Create your views here.

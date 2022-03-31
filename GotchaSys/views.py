from django.shortcuts import render
from django.http import HttpResponse

def MainPage(request):
	return HttpResponse('<html><title>Contact Tracing List</title></html>')
# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def calendar(request):
    # Page from the theme 
    return render(request, 'pages/calendar.html')

def index(request):
    # Page from the theme
    return render(request, 'pages/index.html')
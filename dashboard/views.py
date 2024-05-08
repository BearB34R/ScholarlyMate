from django.shortcuts import render
from django.http import HttpResponse

def calendar(request):
    # Page from the theme 
    return render(request, 'pages/calendar.html')

def index(request):
    # Page from the theme
    return render(request, 'pages/index.html')
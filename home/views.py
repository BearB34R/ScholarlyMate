from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login(request):
    # Page from the theme
    return render(request, 'accounts/login.html')

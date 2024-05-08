from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    # Page from the theme
    return render(request, 'accounts/login.html')

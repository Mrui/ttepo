from django.shortcuts import render
from django.http import *
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .models import *


# Create your views here.

def frontpage(request):
    return render(request, 'www/frontpage.html')

def board(request):
    return render(request, 'www/frontpage.html')

def concept(request):
    return render(request, 'www/frontpage.html')

def gallery(request):
    return render(request, 'www/frontpage.html')

def publications(request):
    return render(request, 'www/frontpage.html')

def faq(request):
    return render(request, 'www/frontpage.html')

def links(request):
    return render(request, 'www/frontpage.html')

def map(request):
    return render(request, 'www/frontpage.html')

def feedback(request):
    return render(request, 'www/frontpage.html')
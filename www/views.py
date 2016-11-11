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
    return render(request, 'www/concept.html')

def gallery(request):
    return render(request, 'www/frontpage.html')

def publications(request):
    return render(request, 'www/publications.html')

def faq(request):
    return render(request, 'www/faq.html')

def irc(request):
    return render(request, 'www/irc_ohje.html')

def links(request):
    return render(request, 'www/links.html')

def map(request):
    return render(request, 'www/frontpage.html')

def feedback(request):
    return render(request, 'www/frontpage.html')
from django.shortcuts import render
from django.http import *
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from datetime import date
from .models import *


# Create your views here.

def frontpage(request):
	news = News.objects.all()
	return render(request, 'www/frontpage.html', {'news': news})

def board(request):
	try:
		boards = Board.objects.all()
		board = Board.objects.latest('year')
		members = board.boardmembers.all()
		return render(request, 'www/board.html', {'boards': boards, 'board':board, 'members': members})
	except:
		return render(request, 'www/board.html')

def oldboard(request, board):
	return render(request, 'www/board.html')

def gallery(request):
    return render(request, 'www/frontpage.html')

def feedback(request):
	return render(request, 'www/frontpage.html')
from django.shortcuts import render
from django.http import *
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from datetime import date
from .models import *
from .forms import *


# Create your views here.

def frontpage(request):
	news = News.objects.all()[:5]
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
	try:
		boards = Board.objects.all()
		board = Board.objects.get(year = board)
		members = board.boardmembers.all()
		return render(request, 'www/board.html', {'boards': boards, 'board':board, 'members': members})
	except:
		return render(request, 'www/board.html')

def gallery(request):
    return render(request, 'www/gallery.html')

def feedback(request):
	return render(request, 'www/feedback.html')

@login_required
def addnews(request):
	if request.method == 'POST':
		form = NewsForm(request.POST)
		if form.is_valid():
			news = form.save(commit=False)
			news.author = request.user
			news.save()
			return HttpResponseRedirect('/')
	args = {}
	args['form'] = NewsForm()
	return render(request, 'www/addnews.html', args)

@login_required
def addboard(request):
	return render(request, 'www/frontpage.html')

@login_required
def addmember(request):
	if request.method == 'POST':
		form = MemberForm(request.POST)
		if form.is_valid():
			news = form.save(commit=False)
			news.author = request.user
			news.save()
			return HttpResponseRedirect('/')
	args = {}
	args['form'] = MemberForm()
	return render(request, 'www/addmember.html', args)
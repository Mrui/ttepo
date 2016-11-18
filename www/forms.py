from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User   # fill in custom user info then save it
from django.contrib.auth.forms import UserCreationForm
from .models import News, Board, BoardMember

class NewsForm(ModelForm):
	class Meta:
		model = News
		fields = ['title', 'text']


class MemberForm(ModelForm):
	class Meta:
		model = BoardMember
		fields = ['role', 'view_order', 'first_name', 'last_name', 'email', 'ircnick', 'photo', 'board']
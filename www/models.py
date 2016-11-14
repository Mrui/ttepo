from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Infobox(models.Model):
	title = models.CharField(max_length = 255, blank = False)
	text = models.TextField()
	date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title

class News(models.Model):
	title = models.CharField(max_length = 255, unique = False)
	text = models.TextField()
	author = models.ForeignKey('auth.User')
	date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title + ' ' + self.date

class Comment(models.Model):
	comment_to = models.ForeignKey(News, related_name='comments')
	text = models.TextField()
	name = models.CharField(max_length = 255, blank = False)
	date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.comment.to.title + ' ' + self.date

class Board(models.Model):
	year = models.IntegerField(unique=True, blank=False, null=False)

	def __str__(self):
		return self.year

class BoardMember(models.Model):
	role = models.CharField(max_length = 255, blank = False, unique = False)
	first_name = models.CharField(max_length = 255)
	last_name = models.CharField(max_length = 255)
	email = models.EmailField(default='etu.suku@student.tut.fi')
	ircnick = models.CharField(max_length = 15)
	photo = models.ImageField(upload_to = '/board/')
	board = models.ForeignKey(Board, related_name='boardmembers')

	def __str__(self):
		return self.last_name + ' ' + self.first_name

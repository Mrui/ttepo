from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Infobox(models.Model):
	title = models.CharField(max_length = 255, blank = False)
	text = models.TextField()
	date = models.DateTimeField(default=timezone.now)

	class Meta:
		verbose_name_plural = "Infoboxes"
	def __str__(self):
		return self.title

class News(models.Model):
	title = models.CharField(max_length = 255, unique = False)
	text = models.TextField()
	author = models.ForeignKey('auth.User')
	date = models.DateTimeField(default=timezone.now)

	class Meta:
		ordering = ['-date']
		verbose_name_plural = "News"

	def __str__(self):
		return self.title + ' ' + str(self.date)

class Board(models.Model):
	year = models.IntegerField(unique=True, blank=False)

	class Meta:
		ordering = ['-year']

	def __str__(self):
		return str(self.year)

class BoardMember(models.Model):

	BOARDROLES = (
		('Puheenjohtaja', 'Puheenjohtaja'),
		('Varapuheenjohtaja', 'Varapuheenjohtaja'),
		('Rahastonhoitaja', 'Rahastonhoitaja'),
		('Sihteeri', 'Sihteeri'),
		('Tiedotus- ja fuksivastaava', 'Tiedotus- ja fuksivastaava'),
		('Liikunta- ja huvivastaava', 'Liikunta- ja huvivastaava'),
		('Isäntä', 'Isäntä'),
		('Emäntä', 'Emäntä'),
		('Varajäsen', 'Varajäsen'),
		('Toimari', 'Toimari'),
		('Kooraaja', 'Kooraaja'),
		)
	BOARDVIEW_ORDER = (
		(1, 'Puheenjohtaja'),
		(2, 'Varapuheenjohtaja'),
		(3, 'Rahastonhoitaja'),
		(4, 'Sihteeri'),
		(5, 'Tiedotus- ja fuksivastaava'),
		(6, 'Liikunta- ja huvivastaava'),
		(7, 'Isäntä'),
		(8, 'Emäntä'),
		(9, 'Varajäsen'),
		(10, 'Toimari'),
		(11, 'Kooraaja'),
		)
	role = models.CharField(max_length=20,
		choices=BOARDROLES, blank=False, null=False)
	view_order = models.IntegerField(
		choices=BOARDVIEW_ORDER, blank=False, null=False)
	first_name = models.CharField(max_length = 255)
	last_name = models.CharField(max_length = 255)
	email = models.EmailField(default='etu.suku@student.tut.fi')
	ircnick = models.CharField(max_length = 15, blank=True)
	photo = models.URLField(blank = True)
	board = models.ForeignKey(Board, related_name='boardmembers')

	class Meta:
		ordering = ['view_order']

	def __str__(self):
		return self.last_name + ' ' + self.first_name

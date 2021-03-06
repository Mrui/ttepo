from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.frontpage, name='frontpage'),
	url(r'^add/news/$', views.addnews, name='addnews'),
	url(r'^add/board/$', views.addboard, name='addboard'),
	url(r'^add/board/member/$', views.addmember, name='addmember'),
	url(r'^board/$', views.board, name="board"),
	url(r'^board/([0-9]+)/$', views.oldboard, name="oldboard"),
	url(r'^gallery/$', views.gallery, name="gallery"),
	# url(r'^publications/$', views.publications, name="publications"),
	# url(r'^faq/$', views.faq, name="faq"),
	# url(r'^faq/irc$', views.irc, name="irc"),
	# url(r'^links/$', views.links, name="links"),
	# url(r'^map/$', views.map, name="map"),
	# url(r'^concept/$', views.concept, name="concept"),
	url(r'^feedback/$', views.feedback, name="feedback"),
	url(r'^pages/', include('django.contrib.flatpages.urls')),
]
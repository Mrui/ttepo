from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.frontpage, name='frontpage'),
	url(r'^board/$', views.board, name="board"),
	url(r'^concept/$', views.concept, name="concept"),
	url(r'^gallery/$', views.gallery, name="gallery"),
	url(r'^publications/$', views.publications, name="publications"),
	url(r'^faq/$', views.faq, name="faq"),
	url(r'^links/$', views.links, name="links"),
	url(r'^map/$', views.map, name="map"),
	url(r'^feedback/$', views.feedback, name="feedback"),
]
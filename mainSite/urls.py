from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from mainSite.models import Candidates
from mainSite import views

urlpatterns = patterns('',
	url(r'^register', views.register),
	url(r'^view$', views.view_candidate),
	url(r'^$', views.logged),
	url(r'^view/(?P<candidateName>[-\w]+)/$',views.candidateView , name = 'candidatePage'),
	(r'^add_candidate/$', views.add_candidate),

	#url(r'^vote', views.tmp),
	url(r'^vote/(?P<candidatePost>[-\w]+)/$',views.candidateDetails, name = 'candidatePost'),
)

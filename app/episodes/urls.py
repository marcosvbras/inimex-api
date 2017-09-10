from django.conf.urls import url
from .views import EpisodeListCreateView, EpisodeRetrieveUpdateView

urlpatterns = [
	url(r'^animes/(?P<anime_pk>\d+)/episodes$', EpisodeListCreateView.as_view(), name='episode_list_create'),
	url(r'^animes/(?P<anime_pk>\d+)/episodes/(?P<episode_pk>\d+)$', 
		EpisodeRetrieveUpdateView.as_view(), name='episode_retrieve_update'),
]
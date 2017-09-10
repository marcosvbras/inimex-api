from django.conf.urls import url
from .views import CharacterListCreateView, CharacterRetrieveUpdateView

urlpatterns = [
	url(r'^animes/(?P<anime_pk>\d+)/characters$', CharacterListCreateView.as_view(), name='character_list_create'),
	url(r'^animes/(?P<anime_pk>\d+)/characters/(?P<character_pk>\d+)$', 
		CharacterRetrieveUpdateView.as_view(), name='character_retrieve_update'),
]
from django.conf.urls import url
from .views import AnimeListCreateView, AnimeUpdateRetriveView

urlpatterns = [
	url(r'^animes/$', AnimeListCreateView.as_view(), name='anime_list_create'),
	url(r'^animes/(?P<anime_pk>\d+)$', AnimeUpdateRetriveView.as_view(), name='anime_update_retrieve'),
]
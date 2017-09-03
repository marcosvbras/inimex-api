from django.conf.urls import url
from .views import GetAnimesView, AnimeListCreateView, AnimeUpdateRetriveView

urlpatterns = [
	url(r'^animes/search$', GetAnimesView.as_view(), name='get_animes'),
	url(r'^animes/$', AnimeListCreateView.as_view(), name='anime_list_create'),
	url(r'^animes/(?P<anime_pk>\d+)$', AnimeUpdateRetriveView.as_view(), name='anime_update_retrieve'),
]
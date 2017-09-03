from django.conf.urls import url
from .views import GenreListCreateView, GenreRetrieveUpdateView

urlpatterns = [
	url(r'^genres/$', GenreListCreateView.as_view(), name='genre_list_create'),
	url(r'^genres/(?P<genre_pk>\d+)$', GenreRetrieveUpdateView.as_view()),
]
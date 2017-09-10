from django.conf.urls import url
from .views import ReviewListCreateView, ReviewRetrieveUpdateView

urlpatterns = [
	url(r'^animes/(?P<anime_pk>\d+)/reviews$', ReviewListCreateView.as_view(), name='review_list_create'),
	url(r'^animes/(?P<anime_pk>\d+)/reviews/(?P<review_pk>\d+)$', ReviewRetrieveUpdateView.as_view(),
		name='review_retrieve_update'),
]
from django.conf.urls import url
from .views import MyListCreateView

urlpatterns = [
	url(r'^users/(?P<user_pk>\d+)/lists/$', MyListCreateView.as_view(), name='mylist_list_create'),
]
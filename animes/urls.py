from django.conf.urls import url
from .views import GetAnimesView

urlpatterns = [
	url(r'^search$', GetAnimesView.as_view(), name="get_animes"),
]
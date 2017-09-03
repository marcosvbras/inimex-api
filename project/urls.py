from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
	url(r'^v1/', include('animes.urls', namespace='animes')),
	url(r'^v1/', include('categories.urls', namespace='categories')),
	url(r'^v1/', include('genres.urls', namespace='genres')),
	url(r'^v1/', include('searches.urls', namespace='searches')),
    url(r'^admin/', admin.site.urls),
]

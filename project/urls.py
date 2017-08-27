from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
	url(r'^animes/', include('animes.urls', namespace='animes')),
    url(r'^admin/', admin.site.urls),
]

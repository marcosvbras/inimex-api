from django.conf.urls import url
from .views import AccountLoginView

urlpatterns = [
	url(r'^login/$', AccountLoginView.as_view(), name='user_authentication'),
]
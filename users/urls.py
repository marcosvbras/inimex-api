from django.conf.urls import url
from .views import UserLoginView

from users import views

urlpatterns = [
	url(r'^authenticate/$', UserLoginView.as_view(), name='user_authentication'),
]
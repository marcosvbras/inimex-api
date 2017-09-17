from django.conf.urls import url
from .views import UserLoginView, UserSignupView

from users import views

urlpatterns = [
	url(r'^authentication/login/$', UserLoginView.as_view(), name='user_login'),
	url(r'^authentication/signup/$', UserSignupView.as_view(), name='user_signup'),
]
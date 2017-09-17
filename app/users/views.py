from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

class UserLoginView(APIView):

	authentication_classes = (TokenAuthentication,)

	def post(self, request):
		username = request.data.get('username')
		password = request.data.get('password')
		user = authenticate(request, username=username, password=password)

		if not user:
			return Response({'error': 'Login failed. Username or password invalid.'})

		token, created = Token.objects.get_or_create(user=user)
		return Response({'token': token.key})


class UserSignupView(APIView):

	def post(self, request):
		pass
		# form = UserCreationForm(request.POST)

		# if form.is_valid():
		# 	form.save()
		# 	username = form.cleaned_data.get('username')
		# 	raw_password = form.cleaned_data.get('password1')
		# 	user.authenticate(request, username=username, password=password)
		# 	token, created = Token.objects.get_or_create(user=user)
		# 	return Response({'token': token.key})

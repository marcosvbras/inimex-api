from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

class AccountLoginView(APIView):

	authentication_classes = (TokenAuthentication,)

	def post(self, request):
		username = request.data.get('username')
		password = request.data.get('password')
		user = authenticate(request, username=username, password=password)

		if not user:
			return Response({'error': 'Login failed. Username or password invalid.'})

		token, created = Token.objects.get_or_create(user=user)
		return Response({'token': token.key})

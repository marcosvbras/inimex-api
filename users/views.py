from django.contrib.auth import authenticate, login
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

class UserLoginView(APIView):

	authentication_classes = (SessionAuthentication, BasicAuthentication,)
	permission_classes = (IsAuthenticated,)

	def get(self, request, format=None):
		content = {
			'user': request.user,
			'auth': request.auth,
		}
		return Response(content)

	# def post(self, request, *args, **kwargs):
	# 	username = request.POST['username']
	# 	password = request.POST['password']
	# 	user = authenticate(request, username=username, password=password)

	# 	if user:
	# 		HttpResponse(login(request, user))
	# 	else:
	# 		HttpResponse("{ error: 'Username or password incorrect}")


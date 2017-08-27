from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from .tasks import get_animes

class GetAnimesView(APIView):
	def post(self, *args, **kwargs):
		get_animes.delay()
		return HttpResponse("Tretou")

from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from django.http import HttpResponse
from .tasks import get_animes
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from .serializers import AnimeSerializer, AnimePagination
from .models import Anime

class AnimeMixim:
	serializer_class = AnimeSerializer
	pagination_class = AnimePagination

	def get_queryset(self):
		return Anime.objects.all()


class AnimeListCreateView(AnimeMixim, ListCreateAPIView):
	pass


class AnimeUpdateRetriveView(AnimeMixim, RetrieveUpdateAPIView):
	lookup_field = 'anime_pk'

	def get_object(self):
		anime_pk = self.kwargs['anime_pk']
		return get_object_or_404(Anime, pk=anime_pk)


class GetAnimesView(APIView):
	def post(self, *args, **kwargs):
		get_animes.delay()
		return HttpResponse("Getting animes")

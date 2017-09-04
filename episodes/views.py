from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from .serializers import EpisodeSerializer, EpisodePagination
from animes.models import Anime
from .models import Episode

class EpisodeMixim:
	serializer_class = EpisodeSerializer
	pagination_class = EpisodePagination

	def get_queryset(self):
		Episode.objects.all()


class EpisodeListCreateView(EpisodeMixim, ListCreateAPIView):
	
	def get_queryset(self):
		anime_pk = self.kwargs['anime_pk']
		anime = get_object_or_404(Anime, pk=anime_pk)
		return Episode.objects.filter(anime=anime)


class EpisodeRetrieveUpdateView(EpisodeMixim, RetrieveUpdateAPIView):
	lookup_field = 'episode_pk'

	def get_object(self):
		anime_pk = self.kwargs['anime_pk']
		episode_pk = self.kwargs['episode_pk']
		return get_object_or_404(Episode, pk=episode_pk, anime__id=anime_pk)


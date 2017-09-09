from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import AnimeSerializer, AnimePagination
from .models import Anime

class AnimeMixim:
	serializer_class = AnimeSerializer
	pagination_class = AnimePagination
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		return Anime.objects.all()


class AnimeListCreateView(AnimeMixim, ListCreateAPIView):
	pass


class AnimeUpdateRetriveView(AnimeMixim, RetrieveUpdateAPIView):
	lookup_field = 'anime_pk'

	def get_object(self):
		anime_pk = self.kwargs['anime_pk']
		return get_object_or_404(Anime, pk=anime_pk)


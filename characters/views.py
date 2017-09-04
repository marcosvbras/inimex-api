from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from .serializers import CharacterSerializer, CharacterPagination
from .models import Character
from animes.models import Anime

class CharacterMixim:
	serializer_class = CharacterSerializer
	pagination_class = CharacterPagination

	def get_queryset(self):
		return Character.objects.all()


class CharacterListCreateView(CharacterMixim, ListCreateAPIView):
	
	def get_queryset(self):
		anime_pk = self.kwargs['anime_pk']
		anime = get_object_or_404(Anime, pk=anime_pk)
		return Character.objects.filter(anime=anime)


class CharacterRetrieveUpdateView(CharacterMixim, RetrieveUpdateAPIView):
	lookup_field = 'character_pk'

	def get_object(self):
		anime_pk = self.kwargs['anime_pk']
		character_pk = self.kwargs['character_pk']
		return get_object_or_404(Character, pk=character_pk, anime__id=anime_pk)



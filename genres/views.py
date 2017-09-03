from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from .models import Genre
from .serializers import GenreSerializer, GenrePagination

class GenreMixim:
	serializer_class = GenreSerializer
	pagination_class = GenrePagination

	def get_queryset(self):
		return Genre.objects.all()


class GenreListCreateView(GenreMixim, ListCreateAPIView):
	pass


class GenreRetrieveUpdateView(GenreMixim, RetrieveUpdateAPIView):
	lookup_field = 'genre_pk'

	def get_object(self):
		genre_pk = self.kwargs['genre_pk']
		return get_object_or_404(Genre, pk=genre_pk)


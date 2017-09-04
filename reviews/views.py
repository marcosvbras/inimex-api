from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from .serializers import ReviewSerializer, ReviewPagination
from .models import Review
from animes.models import Anime

class ReviewMixim:
	serializer_class = ReviewSerializer
	pagination_class = ReviewPagination

	def get_queryset(self):
		Review.objects.all()


class ReviewListCreateView(ReviewMixim, ListCreateAPIView):

	def get_queryset(self):
		anime_pk = self.kwargs['anime_pk']
		anime = get_object_or_404(Anime, pk=anime_pk)
		return get_object_or_404(Review, anime=anime)


class ReviewRetrieveUpdate(ReviewMixim, RetrieveUpdateAPIView):

	def get_object(self):
		anime_pk = self.kwargs['anime_pk']
		review_pk = self.kwargs['review_pk']
		return get_object_or_404(Review, pk=review_pk, anime__pk=anime_pk)
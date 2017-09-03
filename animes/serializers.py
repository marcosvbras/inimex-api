from django.conf import settings
from rest_framework.serializers import ModelSerializer
from rest_framework.pagination import PageNumberPagination
from .models import Anime

class AnimeSerializer(ModelSerializer):

	class Meta:
		model = Anime
		fields = '__all__'


class AnimePagination(PageNumberPagination):
	page_size = settings.ANIME_PAGE_SIZE
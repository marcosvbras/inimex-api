from rest_framework.serializers import ModelSerializer
from rest_framework.pagination import PageNumberPagination
from django.conf import settings
from .models import Episode

class EpisodeSerializer(ModelSerializer):

	class Meta:
		model = Episode
		fields = '__all__'


class EpisodePagination(PageNumberPagination):
	page_size = settings.DEFAULT_PAGE_SIZE

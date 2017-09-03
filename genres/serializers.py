from django.conf import settings
from rest_framework.serializers import ModelSerializer
from rest_framework.pagination import PageNumberPagination
from .models import Genre

class GenreSerializer(ModelSerializer):

	class Meta:
		model = Genre
		fields = '__all__'


class GenrePagination(PageNumberPagination):
	page_size = settings.DEFAULT_PAGE_SIZE
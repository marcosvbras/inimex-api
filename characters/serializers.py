from django.conf import settings
from rest_framework.serializers import ModelSerializer
from rest_framework.pagination import PageNumberPagination
from .models import Character

class CharacterSerializer(ModelSerializer):

	class Meta:
		model = Character
		fields = '__all__'


class CharacterPagination(PageNumberPagination):
	page_size = settings.DEFAULT_PAGE_SIZE
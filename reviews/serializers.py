from rest_framework.serializers import ModelSerializer
from rest_framework.pagination import PageNumberPagination
from django.conf import settings
from .models import Review

class ReviewSerializer(ModelSerializer):

	class Meta:
		model = Review
		fields = '__all__'


class ReviewPagination(PageNumberPagination):
	page_size = settings.DEFAULT_PAGE_SIZE
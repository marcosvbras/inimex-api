from django.conf import settings
from rest_framework.serializers import ModelSerializer
from rest_framework.pagination import PageNumberPagination
from .models import Categorie

class CategorieSerializer(ModelSerializer):

	class Meta:
		model = Categorie
		fields = '__all__'


class CategoriePagination(PageNumberPagination):
	page_size = settings.DEFAULT_PAGE_SIZE
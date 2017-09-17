from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination
from django.conf import settings
from .models import MyList

class MyListSerializer(serializers.ModelSerializer):

	class Meta:
		model = MyList
		fields = '__all__'


class MyListPagination(PageNumberPagination):
	page_size = settings.DEFAULT_PAGE_SIZE
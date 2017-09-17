from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import MyListSerializer, MyListPagination
from .models import MyList

class MyListMixim:
	serializer_class = MyListSerializer
	pagination_class = MyListPagination
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		return MyList.objects.all()


class MyListCreateView(MyListMixim, ListCreateAPIView):

	def get_queryset(self):
		user_pk = self.kwargs['user_pk']
		user = get_object_or_404(User, pk=user_pk)
		return super().get_queryset()


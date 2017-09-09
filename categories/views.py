from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Categorie
from .serializers import CategorieSerializer, CategoriePagination

class CategorieMixim:
	serializer_class = CategorieSerializer
	pagination_class = CategoriePagination
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		return Categorie.objects.all()


class CategorieListCreateView(CategorieMixim, ListCreateAPIView):
	pass


class CategorieRetrieveUpdateView(CategorieMixim, RetrieveUpdateAPIView):
	lookup_field = 'categorie_pk'

	def get_object(self):
		categorie_pk = self.kwargs['categorie_pk']
		return get_object_or_404(Categorie, pk=categorie_pk)

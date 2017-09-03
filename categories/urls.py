from django.conf.urls import url
from .views import CategorieListCreateView, CategorieRetrieveUpdateView

urlpatterns = [
	url(r'^categories/$', CategorieListCreateView.as_view(), name='categories_list_create'),
	url(r'^categories/(?P<categorie_pk>\d+)$', CategorieRetrieveUpdateView.as_view(), name='categories_retrieve_update'),
]
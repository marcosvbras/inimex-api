from django.db import models
from utils.models import DateAbstractModel

class Categorie(DateAbstractModel):

	original_id = models.IntegerField()
	title = models.CharField(max_length=255)
	slug = models.CharField(max_length=255)
	description = models.TextField(blank=True, null=True)
	nsfw = models.BooleanField(default=False)

	def __str__(self):
		return self.title


from django.db import models
from utils.models import DateAbstractModel
from animes.models import Anime

class Character(DateAbstractModel):
	
	anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
	slug = models.CharField(max_length=255)
	name = models.CharField(max_length=255)
	mal_id = models.IntegerField()
	original_id = models.IntegerField()
	description = models.TextField(blank=True, null = True)
	image_url = models.TextField(blank=True, null = True)

	def __str__(self):
		return self.name


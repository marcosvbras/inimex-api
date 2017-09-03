from django.db import models
from utils.models import DateAbstractModel
from animes.models import Anime

class Review(DateAbstractModel):

	anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
	original_id = models.IntegerField()
	content = models.TextField()
	content_formatted = models.TextField(blank=True, null=True)
	likes_count = models.IntegerField()
	rating = models.IntegerField()
	source = models.CharField(max_length=255, blank=True, null=True)
	spoiler = models.BooleanField(default=True)

	def __str__(self):
		return self.content[:20]
	

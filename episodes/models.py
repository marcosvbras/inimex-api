from django.db import models
from utils.models import DateAbstractModel
from animes.models import Anime

class Episode(DateAbstractModel):

	original_id = models.IntegerField()
	english_title = models.CharField(max_length=255, blank=True, null=True)
	original_title = models.CharField(max_length=255, blank=True, null=True)
	canonical_title = models.CharField(max_length=255, blank=True, null=True)
	season_number = models.IntegerField(blank=True, null=True)
	number = models.IntegerField(blank=True, null=True)
	synopsis = models.TextField(blank=True, null=True)
	air_date = models.CharField(max_length=30, blank=True, null=True)
	thumbnail_url = models.TextField(blank=True, null=True)
	length = models.IntegerField(blank=True, null=True)
	anime = models.ForeignKey(Anime, on_delete=models.CASCADE)

	def __str__(self):
		return self.english_title or self.original_title or 'Unknown'

from django.db import models
from utils.models import DateAbstractModel

class Episode(DateAbstractModel):

	original_id = models.IntegerField()
	english_title = models.CharField(max_length=255, blank=True, null=True)
	original_title = models.CharField(max_length=255, blank=True, null=True)
	canonical_title = models.CharField(max_length=255, blank=True, null=True)
	season_number = models.IntegerField()
	number = models.IntegerField()
	synopsis = models.TextField(blank=True, null=True)
	air_date = models.CharField(max_length=30)
	thumbnail_url = models.TextField(blank=True, null=True)
	length = models.IntegerField()

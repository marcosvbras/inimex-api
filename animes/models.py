from django.db import models
from utils.models import DateAbstractModel

class Anime(DateAbstractModel):
	
	original_id = models.IntegerField()
	slug = models.CharField(max_length=255)
	synopsis = models.TextField(blank=True, null=True)
	english_title = models.CharField(max_length=255, blank=True, null=True)
	original_title = models.CharField(max_length=255)
	canonical_title = models.CharField(max_length=255, blank=True, null=True)
	average_rating = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
	start_date = models.CharField(max_length=255, blank=True, null=True)
	end_date = models.CharField(max_length=255, blank=True, null=True)
	age_rating = models.CharField(max_length=50, blank=True, null=True)
	age_rating_guide = models.CharField(max_length=50, blank=True, null=True)
	subtype = models.CharField(max_length=50, blank=True, null=True)
	status = models.CharField(max_length=50, blank=True, null=True)
	poster_image_link = models.TextField(blank=True, null=True)
	cover_image_link = models.TextField(blank=True, null=True)
	episode_count = models.IntegerField(blank=True, null=True)
	episode_length = models.IntegerField(blank=True, null=True)
	youtube_video_id = models.TextField(blank=True, null=True)
	show_type = models.CharField(max_length=50, blank=True, null=True)
	nsfw = models.BooleanField(default=False)
	




from django.db import models
from utils.models import DateAbstractModel
from categories.models import Categorie
from genres.models import Genre

class Anime(DateAbstractModel):
	
	original_id = models.IntegerField()
	english_title = models.CharField(max_length=255, blank=True, null=True)
	original_title = models.CharField(max_length=255, blank=True, null=True)
	slug = models.CharField(max_length=255)
	synopsis = models.TextField(blank=True, null=True)
	canonical_title = models.CharField(max_length=255, blank=True, null=True)
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
	# M2M Fields
	categories = models.ManyToManyField(Categorie)
	genres = models.ManyToManyField(Genre)

	def __str__(self):
		return self.english_title or self.original_title

	




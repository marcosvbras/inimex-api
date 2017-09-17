from django.db import models
from utils.models import DateAbstractModel
from categories.models import Categorie
from genres.models import Genre
from lists.models import MyList

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


class AnimeList(DateAbstractModel):
	
	STATUS_CHOICES = (
		('1', 'Watching'),
		('2', 'Completed'),
		('3', 'Dropped'),
		('4', 'Plan To Watch'),
	)

	RATE_CHOICES = (
		('1', 'Appalling'),
		('2', 'Horrible'),
		('3', 'Very Bad'),
		('4', 'Bad'),
		('5', 'Average'),
		('6', 'Fine'),
		('7', 'Good'),
		('8', 'Very Good'),
		('9', 'Great'),
		('10', 'Masterpiece'),
	)

	anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
	
	mylist = models.ForeignKey(
		MyList, 
		on_delete=models.CASCADE, 
		null = True,
		blank = True
	)

	progress = models.IntegerField(default=0)
	
	status = models.IntegerField(
		choices = STATUS_CHOICES,
		blank = True,
		null = True
	)
	
	rate = models.IntegerField(
		choices = RATE_CHOICES,
		blank = True,
		null = True
	)
	
	start_watch_date = models.DateTimeField(blank=True, null=True)
	finish_watch_date = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return str(anime)


	




from django.db import models
from utils.models import DateAbstractModel
from django.contrib.auth.models import User

class MyList(DateAbstractModel):

	title = models.CharField(max_length=255)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	animes = models.ManyToManyField('animes.Anime', through='animes.AnimeList')

	def __str__(self):
		return self.title


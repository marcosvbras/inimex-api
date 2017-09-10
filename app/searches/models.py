from django.db import models
from utils.models import DateAbstractModel
from animes.models import Anime
from animes.tasks import get_animes
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save

class Search(DateAbstractModel):

	title = models.TextField(max_length=255)
	started_at = models.DateTimeField(blank=True, null=True)
	finished_at = models.DateTimeField(blank=True, null=True)
	failed = models.BooleanField(default=False)
	error_message = models.TextField(blank=True, null=True)
	attempts = models.IntegerField(blank=True, null=True)
	start_id = models.IntegerField(blank=True, null=True)
	end_id = models.IntegerField(blank=True, null=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Search'
		verbose_name_plural = 'Searches'

@receiver(post_save, sender=Search)
def search_saved(sender, instance, **kwargs):
	get_animes.delay(instance.start_id, instance.end_id)
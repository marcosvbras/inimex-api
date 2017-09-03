from django.db import models
from utils.models import DateAbstractModel

class Search(DateAbstractModel):

	title = models.TextField(max_length=255)
	started_at = models.DateTimeField(blank=True, null=True)
	finished_at = models.DateTimeField(blank=True, null=True)
	failed = models.BooleanField(default=False)
	error_message = models.TextField(blank=True, null=True)
	attempts = models.IntegerField(blank=True, null=True)


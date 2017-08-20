from django.db import models
from utils.models import DateAbstractModel

class Genre(DateAbstractModel):

	original_id = models.IntegerField()
	name = models.CharField(max_length=255)
	slug = models.CharField(max_length=255)
	description = models.CharField(max_length=255)

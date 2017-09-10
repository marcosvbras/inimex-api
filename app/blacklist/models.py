from django.db import models
from utils.models import DateAbstractModel
from django.conf import settings

class BlackList(DateAbstractModel):

	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
	ip_address = models.CharField(max_length=255, blank=True, null=True)
	reason = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.user.username or self.ip_address

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import AccountManager

class Account(AbstractBaseUser):

	username = models.CharField(unique=True, max_length=50)
	email = models.EmailField(unique=True)
	first_name = models.CharField(max_length=100, blank=True, null=True)
	last_name = models.CharField(max_length=100, blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	is_admin = models.BooleanField(default=False)
	
	objects = AccountManager()

	# Used on login operation. This will be the default lookup
	# field when searching for users.
	USERNAME_FIELD = 'email'
	# By default, USERNAME_FIELD and password are required
	# in AbstractBaseUser superclass
	REQUIRED_FIELDS = ['username']

	def __str__(self):
		return self.email

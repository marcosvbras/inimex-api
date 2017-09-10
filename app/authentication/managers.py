from django.contrib.auth.models import BaseUserManager

class AccountManager(BaseUserManager):
	"""
	Custom Manager reponsible for control new accounts
	"""

	def create_user(self, email, password=None, **kwargs):
		# Ensure that an email address is set
		if not email:
			raise ValueError('Users must have a valid e-mail address')

		# Ensure that username is set
		if not kwargs.get('username'):
			raise ValueError('Users must have a valid username')

		account = self.model(
			email = self.normalize_email(email),
			username = kwargs.get('username'),
			first_name = kwargs.get('first_name', None),
			last_name = kwargs.get('last_name', None),
		)

		account.set_password(password)
		account.save()

		return account

	def create_superuser(self, email, password=None, **kwargs):
		account = self.create_user(email, password, kwargs)
		account.is_admin = True
		account.save()

		return account
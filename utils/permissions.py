from rest_framework.permissions import BasePermission
from blacklist.models import BlackList
from django.db.models import Q

class BlackListPermission(BasePermission):
	"""
	Global Permission that check if the user exists in BlackList.
	"""

	def has_permission(self, request, view):
		ip_address = request.META['REMOTE_ADDR']
		blacklisted = BlackList.objects.filter(Q(user=request.user) | Q(ip_address=ip_address)).exists()
		return not blacklisted

from django.contrib import admin
from .models import BlackList

@admin.register(BlackList)
class BlackListAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'ip_address', 'reason',)

from django.contrib import admin
from .models import Search

@admin.register(Search)
class SearchAdmin(admin.ModelAdmin):
	
	list_display = ('id', 'title', 'started_at', 'finished_at', 'failed',)

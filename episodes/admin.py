from django.contrib import admin
from .models import Episode

@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):

	list_display = ("id", "english_title", "created_at", "updated_at",)

from django.contrib import admin
from .models import Anime

@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
	list_display = ("id", "original_title", "created_at", "updated_at",)

from django.contrib import admin
from .models import Anime, AnimeList

@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
	list_display = ("id", "original_title", "created_at", "updated_at",)


@admin.register(AnimeList)
class AnimeListAdmin(admin.ModelAdmin):
	list_display = ("id", "anime", "mylist",)

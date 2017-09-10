from django.contrib import admin
from .models import Genre

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
	list_display = ("id", "name", "created_at", "updated_at",)
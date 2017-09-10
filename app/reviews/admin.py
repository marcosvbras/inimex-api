from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

	list_display = ("id", "likes_count", "created_at", "updated_at",)

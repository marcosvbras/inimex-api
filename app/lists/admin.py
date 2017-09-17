from django.contrib import admin
from .models import MyList

@admin.register(MyList)
class MyList(admin.ModelAdmin):
	list_display = ('id', 'title', 'user',)
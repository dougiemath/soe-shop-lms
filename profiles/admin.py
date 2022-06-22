from django.contrib import admin

from .models import UserProfile


@admin.register(UserProfile)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('user',)

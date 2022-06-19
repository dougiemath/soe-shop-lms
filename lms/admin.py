from django.contrib import admin
from django.db import models

from  embed_video.admin  import  AdminVideoMixin
from django_summernote.admin import SummernoteModelAdmin

from .models import Lessons, LessonCategory


@admin.register(Lessons)
class LessonAdmin(SummernoteModelAdmin):
    list_display = ('category', 'name')
    summernote_fields = '__all__'


class LessonCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(LessonCategory, LessonCategoryAdmin)

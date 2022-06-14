from django.contrib import admin
from  embed_video.admin  import  AdminVideoMixin

from .models import Lessons, LessonCategory


@admin.register(Lessons)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('category','name', 'exam_section', 'question_type', 'video', 'upload_questions')

class LessonCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(LessonCategory, LessonCategoryAdmin)

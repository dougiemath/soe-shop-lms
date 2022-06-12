from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from  embed_video.admin  import  AdminVideoMixin

from .models import Lessons, LessonCategory


@admin.register(Lessons)
class LessonAdmin(SummernoteModelAdmin):
    list_display = ('id', 'category','name', 'exam_section', 'question_type', 'video', 'upload_questions')
    summernote_fields = ('exam_description', 'question_overview', 'sample_question_text', 'sample_question_questions', 'question_approach', 'further_study',)

class LessonCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(LessonCategory, LessonCategoryAdmin)

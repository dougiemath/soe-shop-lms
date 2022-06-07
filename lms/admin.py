from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from  embed_video.admin  import  AdminVideoMixin

from .models import ExamSkill


@admin.register(ExamSkill)
class LessonAdmin(SummernoteModelAdmin):
    list_display = ('exam_name', 'exam_section', 'question_type', 'video', 'upload_questions')
    summernote_fields = ('exam_description', 'question_overview', 'sample_question_text', 'sample_question_questions', 'question_approach',)


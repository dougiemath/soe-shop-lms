from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Category, Course
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('friendly_name', 'name')
    ordering = ('friendly_name',)


@admin.register(Course)
class CourseAdmin(SummernoteModelAdmin):
    list_display = ('name', 'course_length')
    summernote_fields = ('card_description','description')

admin.site.register(Category, CategoryAdmin)


from django.contrib import admin

from .models import Category, Course


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('friendly_name', 'name')
    ordering = ('friendly_name',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'course_length')

admin.site.register(Category, CategoryAdmin)

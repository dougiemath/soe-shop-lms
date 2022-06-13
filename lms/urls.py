from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.lms , name='lms'),
    path('<int:lesson_id>/', views.lms_content, name='lms_content'), 
    path('add/', views.add, name='add'),
    path('add_lesson/', views.add_lesson, name='add_lesson'),
    path('add_lesson_category/', views.add_lesson_category, name='add_lesson_category'),
    path('add_new_shop_course/', views.add_new_shop_course, name='add_new_shop_course'),
    path('manage/', views.manage, name='manage'),
    path('edit/<int:lesson_id>/', views.edit_lesson, name='edit_lesson'),
    path('delete/<int:lesson_id>/', views.delete_lesson, name='delete_lesson'),
    path('edit_shop_content/<int:course_id>', views.edit_shop_content, name='edit_shop_content'),
]

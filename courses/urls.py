from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.courses, name='courses'),
    path('<course_id>/', views.course_details, name='course_details'), 
]
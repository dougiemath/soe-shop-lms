from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.lms , name='lms'),
    path('<examskill_id>/', views.lms_content, name='lms_content'), 

]

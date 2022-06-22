from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('contact_inbox/', views.contact_inbox, name='contact_inbox'),
    path('delete/<contact_id>/', views.delete_email, name='delete_email'),
    path('<contact_id>/', views.contact_received_email,
         name='contact_received_email'),
]

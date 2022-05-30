from django.shortcuts import render

# Create your views here.

def index(request):
    """A view to return the home page"""
    return render(request, 'home/index.html')

def privacy_policy(request):
    """A view to return the privacy policy page."""
    return render(request, 'home/privacy_policy.html')

def terms_and_conditions(request):
    """A view to return the terms and conditions page."""
    return render(request, 'home/terms_and_conditions.html')
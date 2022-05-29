from django.shortcuts import render

from . models import Course, Category
# Create your views here.

def courses(request):
    """A view to return the terms and conditions page."""

    courses = Course.objects.all()

    context = {
        'courses': courses,
    }

    return render(request, 'courses/courses.html', context)

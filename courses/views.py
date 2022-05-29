from django.shortcuts import render, get_object_or_404

from . models import Course, Category
# Create your views here.

def courses(request):
    """A view to return page which will display all the courses 
    that are available."""

    courses = Course.objects.all()

    context = {
        'courses': courses,
    }

    return render(request, 'courses/courses.html', context)


def course_details(request, course_id):
    """A view to return details for each course/type."""

    course = get_object_or_404(Course, pk=course_id)

    context = {
        'course': course,
    }

    return render(request, 'courses/course_details.html', context)
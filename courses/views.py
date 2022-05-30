from django.shortcuts import render, get_object_or_404, reverse
from django.db.models import Q

from . models import Course, Category

def courses(request):
    """A view to return page which will display all the courses 
    that are available and filter/sort."""

    courses = Course.objects.all()
    query = None
    categories = None

    if request.GET:

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            courses = courses.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                return redirect(reverse('courses'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            courses = courses.filter(queries)

    context = {
        'courses': courses,
        'search_term': query,
        'current_categories': categories
    }

    return render(request, 'courses/courses.html', context)


def course_details(request, course_id):
    """A view to return details for each course/type."""

    course = get_object_or_404(Course, pk=course_id)

    context = {
        'course': course,
    }

    return render(request, 'courses/course_details.html', context)
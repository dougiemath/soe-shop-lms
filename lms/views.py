from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import CourseSkill
from profiles.models import UserProfile
from courses.models import Course

@login_required
def lms(request):

    courseskills = CourseSkill.objects.all()
    user = get_object_or_404(UserProfile, user=request.user)
    profile = get_object_or_404(UserProfile, user=request.user)
    courses = profile.course_bought.all()
    print(courseskills)
    print(profile.course_bought)
    print(user)

    if courseskills not in courses:
        print(courseskills)

    context = {
        'courseskills': courseskills,
    }

    return render(request, 'lms/lms.html', context)


def lms_content(request, courseskill_id):
    """A view to return details for each course/type."""

    courseskill = get_object_or_404(CourseSkill, pk=courseskill_id)
    print(courseskill_id)
    profile = get_object_or_404(UserProfile, user=request.user)
    print(profile)
    courses = profile.course_bought.all()
    print(courses)
    current_course = get_object_or_404(Course, courseskill=courseskill)
    print(current_course)
    if current_course not in courses:
        
        messages.error(request, 'You cannot access this page without buying the course.')
        return redirect('lms')

    
    context = {
        'courseskill': courseskill,
    }

    return render(request, 'lms/lms_content.html', context)
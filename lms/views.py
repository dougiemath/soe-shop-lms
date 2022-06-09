from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import ExamSkill
from profiles.models import UserProfile
from courses.models import Course

@login_required
def lms(request):

    examskills = ExamSkill.objects.all()
    user = get_object_or_404(UserProfile, user=request.user)
    profile = get_object_or_404(UserProfile, user=request.user)
    courses = profile.course_bought.all()
    print(examskills)
    print(profile.course_bought)
    print(user)

    if examskills not in courses:
        print(examskills)

    context = {
        'examskills': examskills,
    }

    return render(request, 'lms/lms.html', context)


def lms_content(request, examskill_id):
    """A view to return details for each course/type."""

    examskill = get_object_or_404(ExamSkill, pk=examskill_id)
    print(examskill_id)
    profile = get_object_or_404(UserProfile, user=request.user)
    print(profile)
    courses = profile.course_bought.all()
    print(courses)
    current_course = get_object_or_404(Course, examskill=examskill)
    print(current_course)
    if current_course not in courses:
        
        messages.error(request, 'You cannot access this page without buying the course.')
        return redirect('lms')

    
    context = {
        'examskill': examskill,
    }

    return render(request, 'lms/lms_content.html', context)
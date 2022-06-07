from django.shortcuts import render, get_object_or_404, redirect

from .models import ExamSkill
from profiles.models import UserProfile
from courses.models import Course

def lms(request):

    examskills = ExamSkill.objects.all()
    user = get_object_or_404(UserProfile, user=request.user)

    context = {
        'examskills': examskills,
    }

    return render(request, 'lms/lms.html', context)


def lms_content(request, examskill_id):
    """A view to return details for each course/type."""

    examskill = get_object_or_404(ExamSkill, pk=examskill_id)
    profile = get_object_or_404(UserProfile, user=request.user)
    courses = profile.course_bought.all()
    current_course = get_object_or_404(Course, examskill=examskill)
    # current_course = get_object_or_404(Course, id=?)
    if current_course not in courses:
        return redirect('index')
    
    context = {
        'examskill': examskill,
    }

    return render(request, 'lms/lms_content.html', context)
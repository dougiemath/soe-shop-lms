from django.shortcuts import render, get_object_or_404

from .models import ExamSkill

def lms(request):

    examskills = ExamSkill.objects.all()

    context = {
        'examskills': examskills,
    }

    return render(request, 'lms/lms.html', context)


def lms_content(request, examskill_id):
    """A view to return details for each course/type."""

    examskill = get_object_or_404(ExamSkill, pk=examskill_id)
    
    context = {
        'examskill': examskill,
    }

    return render(request, 'lms/lms_content.html', context)
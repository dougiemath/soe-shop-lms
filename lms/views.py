from django.shortcuts import render, get_object_or_404

from .models import ExamSkill

def lms(request):

    examskills = ExamSkill.objects.all()

    context = {
        'examskills': examskills,
    }

    return render(request, 'lms/lms.html', context)
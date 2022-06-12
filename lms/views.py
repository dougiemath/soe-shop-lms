# from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required

# from .models import CourseSkill
# from profiles.models import UserProfile
# from courses.models import Course

# @login_required
# def lms(request):

#     courseskills = CourseSkill.objects.all()
#     user = get_object_or_404(UserProfile, user=request.user)
#     profile = get_object_or_404(UserProfile, user=request.user)
#     courses = profile.course_bought.all()
#     print(courseskills)
#     print(profile.course_bought)
#     print(user)

#     if courseskills not in courses:
#         print(courseskills)

#     context = {
#         'courseskills': courseskills,
#     }

#     return render(request, 'lms/lms.html', context)


# def lms_content(request, courseskill_id):
#     """A view to return details for each course/type."""

#     courseskill = get_object_or_404(CourseSkill, uuid=uuid)
#     print(courseskill)
#     profile = get_object_or_404(UserProfile, user=request.user)
#     print(profile)
#     courses = profile.course_bought.all()
#     print(courses)
#     # current_course = get_object_or_404(Course, courseskill=courseskill)
#     # print(current_course)
#     # if current_course not in courses:
        
#     #     messages.error(request, 'You cannot access this page without buying the course.')
#     #     return redirect('lms')

    
#     context = {
#         'courseskill': courseskill,
#     }

#     return render(request, 'lms/lms_content.html', context)



from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import CourseSkill, CourseCategory
from profiles.models import UserProfile
from courses.models import Course

@login_required
def lms(request):

    courseskills = CourseSkill.objects.all()
    user = get_object_or_404(UserProfile, user=request.user)
    #profile = get_object_or_404(UserProfile, user=request.user)
    profile = UserProfile.objects.get(user=request.user)
    course_categories = CourseSkill.objects.filter(category=1)
    courses = profile.course_bought.all()
    categorys = CourseCategory.objects.all()
    print("---------------")
    print("COURSE SKILLS: ", courseskills)
    print("---------------")
    print("COURSE CATEGORIES: ", course_categories)
    print("---------------")
    print("CATEGORIES: ", categorys)
    print("---------------")
    print(user)

    if courseskills not in courses:
        print(courseskills)

    context = {
        'courseskills': courseskills,
        'user':user,
        'categorys': categorys,
        'courses': courses
    }

    return render(request, 'lms/lms.html', context)


def lms_content(request, courseskill_id):
    """A view to return details for each course/type."""

    courseskill = get_object_or_404(CourseSkill, pk=courseskill_id)
    coursenum = courseskill.course_num
    print("UUID: ", coursenum)
    profile = get_object_or_404(UserProfile, user=request.user)
    print("PROFILE: ", profile)
    courses = profile.course_bought.all()
    print("COURSES: ", courses)
    current_course = get_object_or_404(Course, courseskill=courseskill)
    print("CURRENT COURSE: ", current_course)
    if current_course not in courses:
        
        messages.error(request, 'You cannot access this page without buying the course.')
        return redirect('lms')

    
    context = {
        'courseskill': courseskill,
    }

    return render(request, 'lms/lms_content.html', context)



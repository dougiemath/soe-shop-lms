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

from .models import Lessons, LessonCategory
from profiles.models import UserProfile
from courses.models import Course

@login_required
def lms(request):

    lessons = Lessons.objects.all()

    user = get_object_or_404(UserProfile, user=request.user)
    #profile = get_object_or_404(UserProfile, user=request.user)
    profile = UserProfile.objects.get(user=request.user)
    course_categories = Lessons.objects.filter(category=1)
    courses_bought = profile.course_bought.all()
    lesson_category = LessonCategory.objects.all()
    print("---------------")
    print("LESSONS: ", lessons)
    print("---------------")
    print("COURSE CATEGORIES: ", course_categories)
    print("---------------")
    print("CATEGORIES: ", lesson_category)
    print("---------------")
    print(user)

    # for lesson in lessons:
    #     for course in courses_bought:
    #         if course.course_category == lesson.category:
    #             print(course)

    if lessons not in courses_bought:
        print(lessons)

    context = {
        'lessons': lessons,
        'user': user,
        'lesson_category': lesson_category,
        'courses_bought': courses_bought
    }

    return render(request, 'lms/lms.html', context)


def lms_content(request, lessons_id):
    """A view to return details for each course/type."""

    lessons = get_object_or_404(Lessons, pk=lessons_id)
    coursenum = lessons.course_num
    print("UUID: ", coursenum)
    profile = get_object_or_404(UserProfile, user=request.user)
    print("PROFILE: ", profile)
    courses = profile.course_bought.all()
    print("COURSES: ", courses)
    current_course = get_object_or_404(Course, lessons=lessons)
    print("CURRENT COURSE: ", current_course)
    if current_course not in courses:
        
        messages.error(request, 'You cannot access this page without buying the course.')
        return redirect('lms')

    
    context = {
        'lessons': lessons,
    }

    return render(request, 'lms/lms_content.html', context)



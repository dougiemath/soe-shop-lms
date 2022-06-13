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



from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Lessons, LessonCategory
from.forms import LessonForm, LessonCategoryForm, NewShopCourseForm
from profiles.models import UserProfile
from courses.models import Course

@login_required
def lms(request):

    lessons = Lessons.objects.all()
    user = get_object_or_404(UserProfile, user=request.user)
    profile = UserProfile.objects.get(user=request.user)
    course_categories = Lessons.objects.filter(category=1)
    courses_bought = profile.course_bought.all()
    lesson_category = LessonCategory.objects.all()
    print("---------------")
    # print("LESSONS: ", lessons)
    # print("---------------")
    # print("COURSE CATEGORIES: ", course_categories)
    # print("---------------")
    # print("CATEGORIES: ", lesson_category)
    # print("---------------")
    # print(user)
    print(Lessons)

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


def lms_content(request, lesson_id):
    """A view to return details for each course/type."""
    print("Content")
    lesson = get_object_or_404(Lessons, pk=lesson_id)
    coursenum = lesson.course_num
    lesson_category = lesson.category
    print("LESSON CATEGORY: ", lesson_category)
    print("UUID: ", coursenum)
    profile = get_object_or_404(UserProfile, user=request.user)
    print("PROFILE: ", profile)
    courses_bought = profile.course_bought.all()
    print("COURSES: ", courses_bought)
    print("LESSON: ", lesson.category)
    
    current_course = Course.objects.all()
    print("00000000000000000000000", current_course)


    # for course in courses_bought:
    #     print(course, lesson_category)
    #     access = course
    #     print("888888888888888888888888", access)
    #     if lesson_category == course.course_category:
    #         print("yep")
    #     else:
    #         print("nope")
            


    # current_course = get_object_or_404(Course, lesson=lesson)
    # print("CURRENT COURSE: ", current_course)
    # if current_course not in courses:
        
    #     messages.error(request, 'You cannot access this page without buying the course.')
    #     return redirect('lms')

    
    context = {
        'lesson': lesson,
    }

    return render(request, 'lms/lms_content.html', context)


def add(request):
    """returns a contents-style page for 
    adding new course/shop content"""
    return render(request, 'lms/add.html')


# .......................................

def add_lesson(request):
    """ Add a lesson to the LMS """
    if request.method == "POST":
        form = LessonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully added lesson")
            return redirect(reverse('add'))
        else:
            messages.error(request, 'Failed to add lesson.  Please check the form.')
        
    else:
        form = LessonForm()


    form = LessonForm()
    template = 'lms/add_lesson.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


    # .......................................

def add_lesson_category(request):
    """ Add a lesson category to the LMS """
    if request.method == "POST":
        form = LessonCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully added lesson category")
            return redirect(reverse('add'))
        else:
            messages.error(request, 'Failed to add lesson category.  Please check the form.')
        
    else:
        form = LessonCategoryForm()


    form = LessonCategoryForm()
    template = 'lms/add_lesson_category.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


# .......................................

def add_new_shop_course(request):
    """ Add a lesson category to the LMS """
    if request.method == "POST":
        form = NewShopCourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully added content to Shop")
            return redirect(reverse('add'))
        else:
            messages.error(request, 'Failed to add content to shop.  Please check the form.')
        
    else:
        form = NewShopCourseForm()


    form = NewShopCourseForm()
    template = 'lms/add_new_shop_course.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit(request):
    """returns a contents-style page for 
    editing course/shop content"""
    lessons = Lessons.objects.all().order_by('category')
    lesson_category = LessonCategory.objects.all()

    context = {
        'lessons': lessons,
        'lesson_category': lesson_category,

    }

    return render(request, 'lms/edit.html', context)

def edit_lesson(request, lesson_id):
    
    lesson = get_object_or_404(Lessons, pk=lesson_id)
    
    if request.method == 'POST':
        form = LessonCategoryForm(request.POST, request.FILES, instance=lesson)
        if form.is_valid():
            form.save()
            messages.success(request, 'Success!')
            return redirect(reverse('edit'))
        else:
            messages.error(request, 'Failed.')
    else:
        form = LessonCategoryForm(instance=lesson)
        messages.info(request, f'You are editing {lesson.name}')

    template = 'lms/edit_lesson.html'

    context = {
        'form': form,
        'lesson': lesson,
    }

    return render(request, template, context)

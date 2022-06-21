from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Lessons, LessonCategory
from.forms import LessonForm, LessonCategoryForm, NewShopCourseForm
from profiles.models import UserProfile
from courses.models import Course


@login_required
def lms(request):
    """displays a contents page for all courses 
    that have been bought by the user"""
    lessons = Lessons.objects.all().order_by('-category')
    profile = UserProfile.objects.get(user=request.user)
    course_categories = Lessons.objects.filter(category=1)
    courses_bought = profile.course_bought.all()
    lesson_category = LessonCategory.objects.all()

    context = {
        'lessons': lessons,
        'profile': profile,
        'lesson_category': lesson_category,
        'courses_bought': courses_bought
    }

    return render(request, 'lms/lms.html', context)


@login_required
def lms_content(request, lesson_id):
    """A view to return details for each course/type."""
    lesson = get_object_or_404(Lessons, pk=lesson_id)
    coursenum = lesson.course_num
    current_course = lesson.category
    profile = get_object_or_404(UserProfile, user=request.user)
    courses_bought = profile.course_bought.all()

    context = {
        'lesson': lesson,
    }

    if request.user.is_superuser:
        return render(request, 'lms/lms_content.html', context)
    elif str(current_course) not in str(courses_bought):
        messages.error(request, 'You do not have access to this page.')
        return redirect('lms')  

    return render(request, 'lms/lms_content.html', context)


@login_required
def manage(request):
    """returns a contents-style page for 
        editing course/shop content"""
    if request.user.is_superuser:
        lessons = Lessons.objects.all().order_by('category')
        lesson_category = LessonCategory.objects.all()
        courses = Course.objects.all()

        context = {
            'lessons': lessons,
            'lesson_category': lesson_category,
            'courses': courses,

        }

        return render(request, 'lms/manage.html', context)
    else:
        messages.error(request, 'You do not have access to this page.')
        return redirect(reverse('index'))


@login_required
def add_lesson(request):
    """ Add a lesson to the LMS """
    if request.user.is_superuser:
        if request.method == "POST":
            form = LessonForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Successfully added lesson")
                return redirect(reverse('manage'))
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
    else:
        messages.error(request, 'You do not have access to this page.')
        return redirect(reverse('index'))


@login_required
def add_lesson_category(request):
    """ Add a lesson category to the LMS """
    if request.user.is_superuser:
        courses = Course.objects.all()
        if request.method == "POST":
            form = LessonCategoryForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Successfully added lesson category")
                return redirect(reverse('manage'))
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
    else:
        messages.error(request, 'You do not have access to this page.')
        return redirect(reverse('index'))


@login_required
def add_new_shop_course(request):
    """ Add a new product to the shop """
    if request.user.is_superuser:
        if request.method == "POST":
            form = NewShopCourseForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Successfully added content to Shop")
                return redirect(reverse('manage'))
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
    else:
        messages.error(request, 'You do not have access to this page.')
        return redirect(reverse('index'))


@login_required
def edit_lesson(request, lesson_id):
    """Allows user to edit the content of a pre-created lesson"""
    if request.user.is_superuser:
        lesson = get_object_or_404(Lessons, pk=lesson_id)
        if request.method == 'POST':
            form = LessonForm(request.POST, request.FILES, instance=lesson)
            if form.is_valid():
                form.save()
                messages.success(request, 'Success!')
                return redirect(reverse('manage'))
            else:
                messages.error(request, 'Failed.')
        else:
            form = LessonForm(instance=lesson)
            messages.info(request, f'You are editing {lesson.name}')

        template = 'lms/edit_lesson.html'

        context = {
            'form': form,
            'lesson': lesson,
        }

        return render(request, template, context)
    else:
        messages.error(request, 'You do not have access to this page.')
        return redirect(reverse('index'))


@login_required
def delete_lesson(request, lesson_id):
    """allows the user to delete an existing lesson"""
    if request.user.is_superuser:
        lesson = get_object_or_404(Lessons, pk=lesson_id)
        lesson.delete()
        messages.success(request, 'Lesson Deleted')
        return redirect(reverse('manage'))
    else:
        messages.error(request, 'You do not have access to this page.')
        return redirect(reverse('index'))


@login_required
def edit_shop_content(request, course_id):
    """allows users to edit the shop's contents"""
    if request.user.is_superuser:
        course = get_object_or_404(Course, pk=course_id)
        if request.method == 'POST':
            form = NewShopCourseForm(request.POST, request.FILES, instance=course)
            if form.is_valid():
                form.save()
                messages.success(request, 'Success!')
                return redirect(reverse('manage'))
            else:
                messages.error(request, 'Failed.')
        else:
            form = NewShopCourseForm(instance=course)
            messages.info(request, f'You are editing {course.name}')

        template = 'lms/edit_shop_content.html'

        context = {
            'form': form,
            'course': course,
        }

        return render(request, template, context)
    else:
        messages.error(request, 'You do not have access to this page.')
        return redirect(reverse('index'))

@login_required
def delete_shop_content(request, course_id):
    """allows the user to delete a product in the shop"""
    if request.user.is_superuser:
        course = get_object_or_404(Course, pk=course_id)
        course.delete()
        messages.success(request, 'Course removed from shop')
        return redirect(reverse('manage'))
    else:
        messages.error(request, 'You do not have access to this page.')
        return redirect(reverse('index'))

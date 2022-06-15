from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from courses.models import Course
from profiles.models import UserProfile

@login_required
def bag(request):
    """A view to return the shopping bag"""
    return render(request, 'bag/bag.html')

@login_required
def add_to_bag(request, item_id):
    """add an item to the shopping bag"""

    course = get_object_or_404(Course, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    profile = UserProfile.objects.get(user=request.user)
    courses_bought = profile.course_bought.all()

    for course_bought in courses_bought:
        if course.name == course_bought.name:
            messages.error(request, f'Our records show that {course.name} has already been purchased.  Please contact us if this is not correct.')
            return redirect(redirect_url)

    if item_id not in list(bag.keys()):
        bag[item_id] = quantity
        messages.success(request, f'Added {course.name} course to bag.')
    else:
        messages.error(request, f'{course.name} has already been added to the bag.')
    
    request.session['bag'] = bag
    return redirect(redirect_url)

@login_required
def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        course = get_object_or_404(Course, pk=item_id)
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        messages.success(request, f'Removed {course.name} from bag.')
        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Something went wrong.  Please try again.')
        return HttpResponse(status=500)
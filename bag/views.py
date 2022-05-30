from django.shortcuts import render, get_object_or_404, redirect, HttpResponse

from courses.models import Course

# Create your views here.

def bag(request):
    """A view to return the shopping bag"""
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """add an item to the shopping bag"""

    course = get_object_or_404(Course, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id not in list(bag.keys()):
        bag[item_id] = quantity
    else:
        print("already added")

    request.session['bag'] = bag
    return redirect(redirect_url)

def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        course = get_object_or_404(Course, pk=item_id)
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
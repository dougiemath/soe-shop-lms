from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    """view to render the checkout page"""
    bag = request.session.get('bag',{})
    if not bag:
        messages.error(request, "You have nothing in your bag at the moment.")
        return redirect(reverse('index'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'

    context = {

        'order_form': order_form

    }

    return render(request, 'checkout/checkout.html', context)
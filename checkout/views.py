from django.shortcuts import render

# Create your views here.
def checkout(request):
    """view to render the checkout page"""
    return render(request, 'checkout/checkout.html')
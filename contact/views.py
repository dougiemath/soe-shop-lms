from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import ContactForm
from.models import Contact

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Thanks for your email, we will contact you shortly.')
            return redirect('index')
 
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact/contact.html', context)

@login_required
def contact_inbox(request):
    """A view to create an inbox style page for emails"""
    if request.user.is_superuser:
        emails = Contact.objects.all()
        print(emails)

        context = {
            'emails': emails,
        }

        return render(request, 'contact/contact_inbox.html', context)
    else:
        messages.error(request, 'You do not have access to this page.')
        return redirect(reverse('index'))

@login_required
def contact_received_email(request, contact_id):
    """A view to give access to full email."""
    if request.user.is_superuser:
        email = get_object_or_404(Contact, pk=contact_id)

        context = {
            'email': email,
        }
        
        return render(request, 'contact/contact_received_email.html', context)
    else:
        messages.error(request, 'You do not have access to this page.')
        return redirect(reverse('index'))
        

@login_required
def delete_email(request, contact_id):
    """allows the user to delete a product in the shop"""
    if request.user.is_superuser:
        email = get_object_or_404(Contact, pk=contact_id)
        email.delete()
        messages.success(request, 'Email deleted')
        return redirect(reverse('contact_inbox'))
    else:
        messages.error(request, 'You do not have access to this page.')
        return redirect(reverse('index'))
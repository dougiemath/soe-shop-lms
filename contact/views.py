from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages


from .forms import ContactForm

# Create your views here.

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'], 
                'message': form.cleaned_data['message'],
                }
            message = "\n".join(body.values())
            
            try:
                send_mail(subject, message, 'website@inquiry.com', ['website@inquiry.com'])
                messages.success(request, f'Your email has been sent.  We will contact you shortly.')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
                
            return redirect(reverse('index'))

    form = ContactForm()
    return render(request, "contact/contact.html", {'form': form})
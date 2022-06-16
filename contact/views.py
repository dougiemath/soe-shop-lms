from django.conf import settings
from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        send_mail(
            message_name, 
            message,  
            message_email,  
            [settings.EMAIL_HOST_USER]
        )

        messages.success(request, f'Thank you {message_name}, we will contact you shortly.')
        return render(request, "contact/contact.html")
    else:
        return render(request, "contact/contact.html")


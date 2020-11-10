from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact
from .forms import ContactForm
import os



def contact(request):

    if request.method == 'POST':

        form = Contact(    
            name = request.POST.get('name'),
            message = request.POST.get('message'),
            email = request.POST.get('email')
        )
        form.save()

        send_mail(
            'New request from secureplus',
            'A new request has been made, log into admin panel to access.',
            os.environ.get('EMAIL'),
            ['djangotest7@outlook.com'],
            fail_silently=False,
        )

    else:

        form = ContactForm()


    context = {
            'form': form
        }

    return render(request, 'contact.html', context)
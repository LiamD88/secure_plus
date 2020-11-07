from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

def contact(request):

    if request.method == 'POST':
        name = request.POST('name')
        message = request.POST('message')
        email = request.POST('email')

        

    return render(request, 'contact.html')
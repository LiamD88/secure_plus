from django.shortcuts import render
from .models import Packages

def services1(request):
    return render(request, 'services1.html')

def oneoff(request):

    packages = Packages.objects.all()

    context = {
        'packages': packages,
    }  

    return render(request, 'oneoff.html', context)

def yearly(request):

    packages = Packages.objects.all()

    context = {
        'packages': packages,
    }  

    return render(request, 'yearly.html', context)

def monthly(request):
    
    packages = Packages.objects.all()

    context = {
        'packages': packages,
    }  


    return render(request, 'monthly.html', context)

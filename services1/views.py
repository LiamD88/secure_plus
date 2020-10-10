from django.shortcuts import render
from .models import Package

def services1(request):

    packages = Package.objects.all()

    context = {
        'packages': packages
    }

    return render(request, 'services1.html', context)

def oneoff(request):

    return render(request, 'oneoff.html')


def monthly(request):
    
    return render(request, 'monthly.html') 

def yearly(request):


    return render(request, 'yearly.html')
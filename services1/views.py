from django.shortcuts import render
from . models import Packages

def services1(request):
    return render(request, 'services1.html')

def oneoff(request):
    return render(request, 'oneoff.html')

def yearly(request):
    return render(request, 'yearly.html')

def monthly(request):
    return render(request, 'monthly.html')

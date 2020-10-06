from django.shortcuts import render
from .models import One, Monthly, Yearly

def services1(request):
    return render(request, 'services1.html')

def oneoff(request):

    one = One.objects.all()

    context = {
        'one': one,
    }  

    return render(request, 'oneoff.html', context)


def monthly(request):
    
    monthly = Monthly.objects.all()

    context = {
        'monthly': monthly,
    }  


    return render(request, 'monthly.html', context)

def yearly(request):

    yearly = Yearly.objects.all()

    context = {
        'yearly': yearly,
    }  

    return render(request, 'yearly.html', context)
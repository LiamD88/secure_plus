from django.shortcuts import render
from .models import Package

def services1(request):

    """ function to render services page packages"""

    packages = Package.objects.all()

    context = {
        'packages': packages,
        'services': 'active'
    }

    return render(request, 'services1.html', context)


from django.shortcuts import render
from django.conf import settings

GOOGLE_MAPS_API_KEY = settings.GOOGLE_MAPS_API_KEY


def about(request):

    context = {
    
    'about': 'active',
    'GOOGLE_MAPS_API_KEY' : settings.GOOGLE_MAPS_API_KEY
    
    }
    
   
    return render(request, 'about.html', context)
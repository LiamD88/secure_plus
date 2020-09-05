from django.shortcuts import render



def about(request):

    GOOGLE_MAPS_API_KEY = 'GOOGLE_MAPS_API_KEY'
   
    return render(request, 'about.html', {'GOOGLE_MAPS_API_KEY': GOOGLE_MAPS_API_KEY})
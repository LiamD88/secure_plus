from django.shortcuts import render


def about(request):

    context = {
    
    'about': 'active',
    'GOOGLE_MAPS_API_KEY' : 'GOOGLE_MAPS_API_KEY'
    
    }
    
   
    return render(request, 'about.html', context)
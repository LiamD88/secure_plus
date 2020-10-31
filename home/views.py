from django.shortcuts import render

context = {
    'home': 'active'
}

def home(request):
    return render(request, 'index.html', context)
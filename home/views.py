from django.shortcuts import render


def home(request):

    """ function to render home page"""

    context = {
    'home': 'active'
}

    return render(request, 'index.html', context)
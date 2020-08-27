from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from .forms import RegistrationForm, LoginForm

def register(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')           
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def login(request):

    if request.method == 'POST':   
        login = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        if user is not None:
                auth.login(request, user)
                return redirect('home')

    else:
        login = LoginForm()

    return render(request, 'login.html', {'form': login})
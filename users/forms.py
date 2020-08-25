from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class RegistrationForm(UserCreationForm):
   

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']



class LoginForm(forms.Form):
    
    username = forms.CharField(
    required=True,)

    password = forms.CharField(
        required=True,
    )


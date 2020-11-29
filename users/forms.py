from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

""" form to register """

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'required': 'True', 'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'required': 'True', 'class': 'form-control', 'placeholder': 'Last Name'}))
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'required': 'True', 'class': 'form-control', 'placeholder': 'Username'}))
    email = forms.CharField(label='', widget=forms.EmailInput(attrs={'required': 'True', 'class': 'form-control', 'placeholder': 'Email'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'required': 'True', 'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'required': 'True', 'class': 'form-control', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email is already registered to another account")
        return email


""" form to login """
class LoginForm(forms.Form):
    
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'required': 'True', 'class': 'form-control', 'placeholder': 'Username' }))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'required': 'True', 'class': 'form-control', 'placeholder': 'Password'}))







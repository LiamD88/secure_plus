from django import forms
from .models import Contact

""" form created for contact page"""

class ContactForm(forms.ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'required': 'True', 'class': 'form-control', 'placeholder': 'Name'}))
    email = forms.CharField(label='', widget=forms.EmailInput(attrs={'required': 'True', 'class': 'form-control', 'placeholder': 'Email'}))
    message = forms.CharField(label='', widget=forms.TextInput(attrs={'required': 'True', 'class': 'form-control', 'placeholder': 'Message'}))
    

    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
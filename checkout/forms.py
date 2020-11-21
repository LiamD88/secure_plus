from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    full_name = forms.CharField(label='', widget=forms.TextInput(attrs={'required': 'True', 'class': 'form-control', 'placeholder': 'Full Name'}))
    email = forms.CharField(label='', widget=forms.EmailInput(attrs={'required': 'True', 'class': 'form-control', 'placeholder': 'Email'}))
    company_name = forms.CharField(label='', widget=forms.TextInput(attrs={'required': 'False', 'class': 'form-control', 'placeholder': 'Company Name'}))
    phone_number = forms.CharField(label='', widget=forms.TextInput(attrs={'required': 'True', 'class': 'form-control', 'placeholder': 'Phone Number'}))
    street_address1 = forms.CharField(label='', widget=forms.TextInput(attrs={'required': 'True', 'class': 'form-control', 'placeholder': 'Street Address 1'}))
    street_address2 = forms.CharField(label='', widget=forms.TextInput(attrs={'required': 'True', 'class': 'form-control', 'placeholder': 'Street Address 2'}))
    town_or_city = forms.CharField(label='', widget=forms.TextInput(attrs={'required': 'True', 'class': 'form-control', 'placeholder': 'Town/City'}))
    country = forms.CharField(label='', widget=forms.TextInput(attrs={'required': 'True', 'class': 'form-control', 'placeholder': 'Country'}))
    postcode = forms.CharField(label='', widget=forms.TextInput(attrs={'required': 'False', 'class': 'form-control', 'placeholder': 'Country'}))


    class Meta:
        model = Order
        fields = ('full_name', 'email', 'company_name', 'phone_number', 'street_address1', 'street_address2', 'town_or_city', 'country', 'postcode')



class PaymentForm(forms.Form):
    credit_card_number = forms.CharField(label='', widget=forms.TextInput(attrs={'required': 'True', 'class': 'form-control', 'placeholder': 'Credit Card Number'}))
    expiry_month = forms.ChoiceField(label='',choices=month_choice, widget=forms.Select(attrs={'required': 'True', 'class': 'form-control'}))
    expiry_year = forms.ChoiceField(label='',choices=year_choice, widget=forms.Select(attrs={'required': 'True', 'class': 'form-control'}))
    cvv= forms.NumberInput(label='', widget=forms.TextInput(attrs={'required': 'True', 'class': 'form-control', 'placeholder': 'CVV'}))

    month_choice = [for i in range(1, 13)]
    year_choice = [for i in range(2020, 2030)]
    

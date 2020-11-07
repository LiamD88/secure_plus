from django import forms



class ContactForm(forms.ModeldForm):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'required': 'True', 'class': 'form-control', 'placeholder': 'Name'}))
    message = forms.CharField(label='', widget=forms.TextInput(attrs={'required': 'True', 'class': 'form-control', 'placeholder': 'Message'}))
    email = forms.CharField(label='', widget=forms.EmailInput(attrs={'required': 'True', 'class': 'form-control', 'placeholder': 'Email'}))

    class Meta:
        model = contact
        fields = ['name', 'message' 'email']
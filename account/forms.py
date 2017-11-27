from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    username = forms.CharField(help_text=None)
    password1 = forms.CharField(help_text=None, widget=forms.PasswordInput(), label='password')
    password2 = forms.CharField(help_text=None, widget=forms.PasswordInput(), label='Retype password')
    user_choice = [
        ('customer', 'customer'),
        ('owner', 'owner'),
        ('staff', 'staff'),     
    ]
    user_type = forms.ChoiceField(choices=user_choice, label='Signup as')

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email', 'user_type']
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, widget=forms.EmailInput())
    username = forms.CharField(help_text=None)
    password1 = forms.CharField(help_text=None, widget=forms.PasswordInput(), label='password')
    password2 = forms.CharField(help_text=None, widget=forms.PasswordInput(), label='Retype password')
    resturent_name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=1000)
    cuisine_choice = (
        ('Continental', 'Continental'),
        ('Indian', 'Indian'),
        ('FastFood', 'FastFood')
    )
    cuisine = forms.MultipleChoiceField(required=True , widget=forms.CheckboxSelectMultiple, choices = cuisine_choice)
    speciality = forms.CharField(max_length=200)
    ExtraCharge = forms.BooleanField()

    vat = forms.BooleanField()
    # opening_time = forms.TimeField()


    # test_choice = (
    #     ('a': 'a'),
    # )
    # test = models.CharField(max_length=30, choice=test_choice)


    class Meta:
        model = User
        fields = ('email','username', 'password1', 'password2', 'resturent_name', 'description', 'cuisine', 'speciality', 'ExtraCharge', 'vat')
        # , 'opening_time'


# class LoginForm(UserCreationForm):
#     # email = forms.EmailField(max_length=254, required=True, widget=forms.EmailInput())
#     username = forms.CharField(help_text=None)
#     password1 = forms.CharField(help_text=None, widget=forms.PasswordInput(), label='password')
#     # password2 = forms.CharField(help_text=None, widget=forms.PasswordInput(), label='password')
#
#     class Meta:
#         model = User
#         fields = ('username','password1')
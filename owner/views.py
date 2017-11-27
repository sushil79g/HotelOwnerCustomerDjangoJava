from django.shortcuts import render, redirect
# from .models import Signup
# from django.http import HttpResponse
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
# from django.contrib import messages
from django.http import HttpResponse
# from django.contrib import  admin
# from django import forms
from .form import SignUpForm
from menu.models import Food, Drink, Order
    # ,LoginForm
# Create your views here.
# def signup(request):
#      new = Signup()
#      new.username = request.username
#      new.email = request.email
#      new.password = request.password
#      new.description = request.description
#      new.token = request.token 
#      new.extra_charge = request.extra_charge
#      new.vat = request.vat
#      new.opening_time = request.opening_time
#      new.closing_time = request.closing_time
#      new.ssid = request.Ssid
#      new.speciality = request.speciality
#      new.save()

# # def login(request):



# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         HttpResponse('yay here1')
#         if form.is_valid():
#             print(form)
#             user = form.save(commit=False)
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password1']
#             form.save()
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             messages.success(request,'user created')
#             # return redirect('register')
#     else:
#         HttpResponse('yay here2')
#         form = UserCreationForm(None)
#     form = Formname()
#     return render(request, 'register.html', {'formabc': form})
#
#
# class Formname(forms.Form):
#     username = forms.CharField(label='username', max_length=150)
#     password1 = forms.PasswordInput( label='password1' ,max_length = 100)
#     password2 = forms.PasswordInput(label='password2', max_length=100)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user.set_password(password)

            user.save()
            user = authenticate(user)

            if user is not None:  # Needs extending #TO DO
                if user.is_active:
                    login(request, user)

            # return redirect('menu:home')
    else:
        form = SignUpForm(None)

    return render(request, 'register.html', {'form': form})


# def login(request):
#     if request.method == 'POST':
#         user = authenticate(username = request.POST['naame'], password = request.POST['passw'])
#         # return  HttpResponse(user)
#         if user=='None':
#             return HttpResponse('you are user')
#         else:
#             return HttpResponse('You are not user')
#         # return HttpResponse(request.POST['naame'])
#     else:
#
#         return render(request, 'login.html', {})
#     # return  render(request,'login.html',{'form':form})



def after(request):
    return  render(request,'afterLogin.html',{})



def order(request):
    if User.is_staff:
        # foodName = request.order_set.all()
        current_user = request.user
        print(current_user.id)

def status(request):
    return  HttpResponse('Kam baki xa yaha')

def menu(request):
    return  HttpResponse('kam baki xa')

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
from menu.models import Food, Drink, FoodOrder, DrinkOrder, SpecialOrder, TodaySpecial
from django.contrib import messages
from datetime import date
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
                if user.is_staff:
                    login(request, user)
            messages.add_message(request, messages.INFO, 'Waiting For Approval')

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
        # today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
        # today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
        today = date.today()
        food = FoodOrder.objects.filter(date = today)
        drink = DrinkOrder.objects.filter(date=today)
        special = SpecialOrder.objects.filter(date=today)
        context={'food':food, 'drink':drink, 'special':special}
        return render(request,'orderlist.html',context)










        # foodName = request.order_set.all()
        # current_user = request.user
        # print(current_user.id)
        # order = Order.objects.all()
        # orders = {'order':order}
        # for ord in order:
        #     print(ord.user)
        # HttpResponse('baki xa hai')
        # return  render(request,'orderlist.html',orders)

def status(request,ispending=0):
    # ispending is value that owner requested to view to view pending list ispending=o and to view delivered list ispending=1

    # only pending list is returned
    if ispending==0:
        today = date.today()
        food = FoodOrder.objects.filter(delivered = False).filter(date = today)
        drink = DrinkOrder.objects.filter(delivered = False).filter(date=today)
        special = SpecialOrder.objects.filter(delivered = False).filter(date=today)
        context = {'food': food, 'drink': drink, 'special': special}
        return render(request, 'orderlist.html', context)


    # only delivered list is returned
    elif ispending==1:
        food = FoodOrder.objects.all(delivered=True)
        drink = DrinkOrder.objects.all(delivered=True)
        special = SpecialOrder.objects.all(delivered=True)
        context = {'food': food, 'drink': drink, 'special': special}
        return render(request, 'orderlist.html', context)

    return  HttpResponse('Kam baki xa yaha')

def menu(request):
    return  HttpResponse('kam baki xa')

def updatePending(request,user_id=0,fid='f'):
    # user_id is the user identification value and fid is the list for updating FoodOrder or drinkorder
    # if fid='f' is food if fid=d is drink
    today = date.today()
    if User.is_staff:
        if fid=='f':
            user = FoodOrder.objects.filter(user=user_id).filter(date=today)
            user.delivered = True

        elif fid=='d':
            user = DrinkOrder.objects.filter(user = user_id).filter(date=today)
            user.delivered = True

    return HttpResponse('yah yah!!!')
    # order = Order.objects.get(pk = person_id)
    # # return HttpResponse(order.user)
    # order.is_delivered = True
    # order.save()
    # return render(request,'orderlist.html',{})






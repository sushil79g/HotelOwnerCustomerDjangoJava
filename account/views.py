from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user_type = form.cleaned_data['user_type']
            user.set_password(password)
            if user_type == 'owner':
                user.is_superuser = True
            elif user_type == 'staff':
                user.is_staff = True
            elif user_type == 'customer':
                user.is_active = True
            user.save()
            user = authenticate(user)
            
            if user is not None: # Needs extending #TO DO
                if user.is_active:
                    login(request, user)
            return redirect('menu:home')
    else:
        form = SignUpForm(None)
    
    return render(request, 'signup.html', {'form': form})
from django.shortcuts import render, redirect
from . forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def home(request):
    return render(request, './home.html')

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account Created Successfully')
            # messages.warning(request, 'Warning')
            # messages.info(request, 'Info')
            form.save()
            print(form.cleaned_data)
    else:
        form = RegisterForm()
    return render(request, './signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data = request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            userpass = form.cleaned_data['password']
            # checking if user exists in database
            user = authenticate(username = name, password = userpass)
            if user is not None:
                login(request, user)
                return redirect('profile')
    else:
        form = AuthenticationForm()
        return render(request, './login.html', {'form': form})

def profile(request):
    return render(request, './profile.html', {'user': request.user})

def user_logout(request):
    logout(request)
    return redirect('login')
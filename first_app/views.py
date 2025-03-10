from django.shortcuts import render, redirect
from . forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
# PasswordChangeForm => needs old password to change current password
# SetPasswordForm => doesn't need old password to change current password
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
# Create your views here.

def home(request):
    return render(request, './home.html')

def signup(request):
    if not request.user.is_authenticated: 
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
    else:
        return redirect('profile')

def user_login(request):
    if not request.user.is_authenticated:
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
    else:
        return redirect('profile')

def profile(request):
    if request.user.is_authenticated:
        return render(request, './profile.html', {'user': request.user})
    else:
        return redirect('login')

def user_logout(request):
    logout(request)
    return redirect('login')

# change password using old password
def pass_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, './passchange.html',{'form':form})
    else:
        return redirect('login')


# change password without using old password
def pass_change2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = SetPasswordForm(user=request.user)
        return render(request, './passchange.html',{'form':form})
    else:
        return redirect('login')
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'id':'required', 'style': 'width: 100%;'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'id':'required', 'style': 'width: 100%;'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'id':'required', 'style': 'width: 100%;'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required', 'style': 'width: 100%;'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required', 'style': 'width: 100%;'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'id':'required', 'style': 'width: 100%;'}))
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

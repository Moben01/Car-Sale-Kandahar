# myapp/forms.py
from allauth.account.forms import SignupForm, LoginForm
from django import forms
from .models import CustomUser
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


User = get_user_model()

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'phone_number', 'password1', 'password2')

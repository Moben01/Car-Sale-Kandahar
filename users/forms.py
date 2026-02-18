# myapp/forms.py
from allauth.account.forms import SignupForm, LoginForm
from django import forms
from .models import UserPhone


class MySignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'نام کاربری شما'})
        self.fields['email'].widget.attrs.update({'placeholder': 'ایمیل شما'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'رمز عبور'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'تکرار رمز عبور'})

class MyLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['login'].widget.attrs.update({'placeholder': 'ایمیل یا نام کاربری'})
        self.fields['password'].widget.attrs.update({'placeholder': 'رمز عبور'})
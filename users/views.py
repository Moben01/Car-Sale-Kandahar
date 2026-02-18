from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from products.models import *
# Create your views here.

def profile(request, id):
    user = User.objects.get(id=id)
    products = NewCar.objects.filter(user=user)

    context = {
        'user':user,
        'products':products,
    }
    return render(request, 'products/profile.html', context)

@login_required
def my_account(request, id):
    user = request.user   # always current user

    phone_obj, created = UserPhone.objects.get_or_create(user=user)

    if request.method == "POST":
        phone_number = request.POST.get('phone_number')

        if phone_number:
            phone_obj.phone_number = phone_number
            phone_obj.save()

        return redirect('users:my_account', id=user.id)

    context = {
        'phone': phone_obj,
    }
    return render(request, 'users/my-account.html', context)
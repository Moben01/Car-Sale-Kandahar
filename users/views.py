from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from products.models import *
from django.contrib import messages
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
    user = request.user  # always current user

    phone_obj, created = UserPhone.objects.get_or_create(user=user)

    if request.method == "POST":
        phone_number = request.POST.get('phone_number')

        if phone_number:
            # simple validation (11 digits example)
            if not phone_number.isdigit() or len(phone_number) < 9:
                messages.error(request, "شماره تماس معتبر نیست.")
            else:
                phone_obj.phone_number = phone_number
                phone_obj.save()
                messages.success(request, "شماره تماس شما با موفقیت ذخیره شد ✅")

        else:
            messages.warning(request, "لطفاً شماره تماس را وارد نمایید.")

        return redirect('users:my_account', id=user.id)

    context = {
        'phone': phone_obj,
    }
    return render(request, 'users/my-account.html', context)
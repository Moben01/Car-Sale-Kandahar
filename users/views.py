from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from products.models import *
from django.contrib.auth import login
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.


def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('username')
            
            user = form.save(commit=False)
            
            base_email = f"{user_name}@temp.com"
            email = base_email
            
            counter = 1
            while CustomUser.objects.filter(email=email).exists():
                email = f"{user_name}{counter}@temp.com"
                counter += 1
            
            user.email = email
            user.save()
            
            backend = settings.AUTHENTICATION_BACKENDS[0]
            login(request, user, backend=backend)
                        
            messages.success(request, f"خوش آمدید {user_name}! حساب کاربری شما با موفقیت ایجاد شد.")
            return redirect("home:dashboard")
        else:
            messages.error(request, "لطفاً خطاهای فرم را تصحیح کنید.")
    else:
        form = SignUpForm()
    
    return render(request, "account/signup.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        phone_number = request.POST.get("phone_number")
        password = request.POST.get("password")
        
        user = None
        
        # Check if using phone number or username
        if phone_number and phone_number.strip():  # Check if phone number is provided and not empty
            # Try login with phone number
            try:
                from .models import CustomUser
                # Get user by phone number
                user_obj = CustomUser.objects.get(phone_number=phone_number)
                # Authenticate using the username from the found user
                user = authenticate(request, username=user_obj.username, password=password)
            except CustomUser.DoesNotExist:
                messages.error(request, "شماره تماس یافت نشد")
                return render(request, "account/login.html")
            except CustomUser.MultipleObjectsReturned:
                messages.error(request, "خطا در سیستم. لطفاً با پشتیبانی تماس بگیرید")
                return render(request, "account/login.html")
        elif username and username.strip():  # Check if username is provided and not empty
            # Try login with username
            user = authenticate(request, username=username, password=password)
        else:
            messages.error(request, "لطفاً نام کاربری یا شماره تماس را وارد کنید")
            return render(request, "account/login.html")
        
        if user and user is not None:
            login(request, user)
            messages.success(request, f"خوش آمدید {user.get_full_name() or user.username}!")
            
            # Redirect to next page or home
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            return redirect("home:dashboard")  # Make sure 'home' is your URL name
        else:
            messages.error(request, "نام کاربری/شماره تماس یا رمز عبور اشتباه است")
    
    return render(request, "account/login.html")


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
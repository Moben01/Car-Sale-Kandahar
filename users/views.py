from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, update_session_auth_hash
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


@login_required
def edit_profile_view(request):
    if request.method == "POST":
        user = request.user
        current_password = request.POST.get('current_password')
        
        # Verify current password
        if not user.check_password(current_password):
            messages.error(request, "رمز عبور فعلی اشتباه است")
            return redirect('account:profile')
        
        # Update username if provided and changed
        new_username = request.POST.get('username')
        if new_username and new_username != user.username:
            if CustomUser.objects.filter(username=new_username).exclude(id=user.id).exists():
                messages.error(request, "این نام کاربری قبلاً استفاده شده است")
                return redirect('account:profile')
            user.username = new_username
        
        # Update phone number if provided and changed
        new_phone = request.POST.get('phone_number')
        if new_phone and new_phone != user.phone_number:
            if CustomUser.objects.filter(phone_number=new_phone).exclude(id=user.id).exists():
                messages.error(request, "این شماره تماس قبلاً ثبت شده است")
                return redirect('account:profile')
            user.phone_number = new_phone
        
        # Update password if provided
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')
        
        if new_password1 or new_password2:
            if new_password1 != new_password2:
                messages.error(request, "رمز عبور جدید و تکرار آن مطابقت ندارند")
                return redirect('account:profile')
            if len(new_password1) < 8:
                messages.error(request, "رمز عبور باید حداقل ۸ کاراکتر باشد")
                return redirect('account:profile')
            user.set_password(new_password1)
        
        # Save changes
        user.save()
        
        # Update session if password was changed
        if new_password1:
            update_session_auth_hash(request, user)
        
        messages.success(request, "اطلاعات حساب کاربری با موفقیت به‌روزرسانی شد")
        return redirect('account:profile')
    
    return redirect('account:profile')


def profile(request, id):
    user = CustomUser.objects.get(id=id)
    products = NewCar.objects.filter(user=user)

    context = {
        'user':user,
        'products':products,
    }
    return render(request, 'products/profile.html', context)


@login_required
def my_account(request, id):
    user = request.user  # always current user


    context = {
        # 'phone': phone_obj,
    }
    return render(request, 'users/my-account.html', context)
from django.shortcuts import render, redirect

# Create your views here.

def dashboard(request):
    return render(request, 'dashboard.html')

def contact_us(request):
    return render(request, 'home/contact-us.html')
from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('contact_us', views.contact_us, name="contact_us"),
]
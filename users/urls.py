from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('profile/<int:id>/', views.profile, name="profile"),
    path('my_account/<int:id>/', views.my_account, name="my_account"),
]
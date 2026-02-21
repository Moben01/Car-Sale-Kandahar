from django.urls import path
from . import views
from .views import signup_view, login_view

urlpatterns = [
    path("signup/", signup_view, name="signup"),
]

app_name = "users"

urlpatterns = [
    path('profile/<int:id>/', views.profile, name="profile"),
    path('my_account/<int:id>/', views.my_account, name="my_account"),
    path("signup/", signup_view, name="signup"),
    path("login/", login_view, name="login"),
]


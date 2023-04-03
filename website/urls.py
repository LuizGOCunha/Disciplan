from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("login/", views.loginv, name="login"),
    path("logout/", views.signout, name="logout"),
    path("activities/", views.activities, name="activities"),
]

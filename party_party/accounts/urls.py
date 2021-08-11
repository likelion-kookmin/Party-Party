from django.contrib import admin
from django.urls.conf import include
from .views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("login/signup/", signup, name="signup"),
]

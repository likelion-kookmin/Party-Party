from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model, authenticate, login, logout
from .forms import *
from .models import UserModel

User = get_user_model()


# Create your views here.
def login(request):
    error = ""
    if request.user.is_authenticated:
        return redirect("main")
    else:
        if request.method == "POST":
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                user = authenticate(
                    request=request, username=username, password=password
                )
                print("user", user, type(user))
                if user is None:
                    print("ddd")
                    error = "오류입니다"
                else:

                    login(request, user)
                    return redirect("main")
            else:
                error = "가입하지 않은 아이디이거나, 잘못된 비밀번호입니다"

        form = AuthenticationForm()
        print("dsafdsf")
        return render(request, "login.html", {"form": form, "error": error})


def logout(request):
    logout(request)
    return redirect("login")


def signup(request):
    if request.user.is_authenticated:
        return redirect("main")

    else:
        if request.method == "POST":
            form = signupForm(request.POST, request.FILES)
            if form.is_valid():
                print("ddddd")
                user = form.save()
                login(request, user)
            return redirect("login")
        else:
            form = signupForm()
            return render(request, "signup.html", {"form": form})

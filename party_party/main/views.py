from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from .models import *

from goods.models import *

User = get_user_model()

def main(request) :
    posts = Goods.objects.all()
    return render(request, 'main.html', {'posts' : posts})
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from .models import *
import datetime

from goods.models import *

User = get_user_model()


def main(request):
    posts = Goods.objects.all()[:4]
    # endneeds = Goods.objects.filter(term_needs = datetime.date.today())
    end_dates = Goods.objects.filter(end_date=datetime.date.today())
    return render(request, 'main.html', {'posts': posts, 'enddeposit': end_dates})

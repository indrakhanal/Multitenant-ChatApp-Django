from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from core.views import login_, logout_


def home(request):
    return render(request, 'public/public.html')


def login_public(request):
    message='cannot login please choose tenant'
    return render(request, 'public/public.html', {'message': message})


def logout_public(request):
    return logout_


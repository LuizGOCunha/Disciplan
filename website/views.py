from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest
from django.db import IntegrityError

from django.contrib.auth import authenticate, login, logout

from .forms import RegistrationForm, LoginForm
from .models import User, Activity

# Create your views here.

def index(request: WSGIRequest) -> HttpResponse:
    context = {}
    if request.user.is_authenticated:
        context['authenticated'] = True
    return render(request, "index.html", context)

def register(request: WSGIRequest) -> HttpResponse:
    context = {}
    context['form'] = RegistrationForm
    context['user'] = request.user

    if request.method == "POST":
        data = request.POST
        if data['password'] == data['password_c']:
            user = User(
                first_name = data['first_name'],
                last_name = data['last_name'],
                email = data['email'],
            )
            user.set_password(data['password'])
            user.full_clean()
            try:
                user.save()
            except IntegrityError:
                context['message'] = 'User Already exists!'
            return redirect('/login/')
        else:
            context['message'] = 'Your passwords do not match.'


    return render(request, "register.html", context)

def loginv(request: WSGIRequest) -> HttpResponse:
    context = {}
    context['form'] = LoginForm
    if request.method == "POST":
        data = request.POST
        user = authenticate(request, username=data['email'], password=data['password'])
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            context['message'] = 'Credentials are invalid. Try again.'
    return render(request, "login.html", context)

def signout(request:WSGIRequest) -> HttpResponse:
    logout(request)
    return redirect("/")
from django.shortcuts import render
from django.http import HttpRequest
from django.core.handlers.wsgi import WSGIHandler

from .forms import RegistrationForm, LoginForm

# Create your views here.

def index(request: WSGIHandler) -> HttpRequest:
    return render(request, "index.html")

def register(request: WSGIHandler) -> HttpRequest:
    context = {}
    context['form'] = RegistrationForm
    return render(request, "register.html", context)

def login(request: WSGIHandler) -> HttpRequest:
    context = {}
    context['form'] = LoginForm
    return render(request, "login.html", context)
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest
from django.db import IntegrityError

from django.contrib.auth import authenticate, login, logout

from .forms import RegistrationForm, LoginForm, ActivitiesForm
from .models import User, Activity

# Create your views here.

def index(request: WSGIRequest) -> HttpResponse:
    context = {}
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

def signout(request: WSGIRequest) -> HttpResponse:
    logout(request)
    return redirect("/")

def activities(request: WSGIRequest) -> HttpResponse:
    context = {}
    if request.user.is_authenticated:
        context['form'] = ActivitiesForm
        context['activities'] = request.user.activities.all()
    else:
        context['message'] = 'You must log in to have access to this page. Log into your account and try again.'
        return redirect('/')
    if request.method == "POST":
        # For deleting activities
        if 'delete' in request.POST.keys():
            id = int(request.POST.get('delete'))
            activity = Activity.objects.get(id=id)
            activity.delete()
        # For adding activities
        else:
            title = request.POST['title']
            difficulty = request.POST['difficulty']
            if 'description' in request.POST.keys():
                description = request.POST['description']
                activity = Activity(title=title, difficulty=difficulty, description=description, user=request.user)
            else:
                activity = Activity(title=title, difficulty=difficulty, user=request.user)
            activity.full_clean()
            activity.save()
        

    return render(request, 'activities.html', context)
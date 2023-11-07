from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect

from user.forms import RegisterForm


def index(request):
    if not request.user.is_authenticated:
        return redirect('/user/login')
    return render(request, 'user/index.html', {})


def user_login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(
            username=username,
            password=password
        )
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return HttpResponseNotFound("Failed to log in")

    return render(request, 'user/user_login.html', {})


def user_logout(request):
    if not request.user.is_authenticated:
        return redirect('/')
    logout(request)

    return redirect("/user/login")


def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/user/login')
    else:
        form = RegisterForm()
    return render(request, 'user/user_register.html', {"form": form})


def rented_lockers(request):
    return "Rented Lockers"


def billing(request):
    return "Billing"

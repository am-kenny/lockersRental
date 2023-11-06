from django.shortcuts import render

# Create your views here.
def index(request):
    return "User"


def login(request):
    return "Login"


def logout(request):
    return "Logout"


def register(request):
    return "Register"


def rented_lockers(request):
    return "Rented Lockers"


def billing(request):
    return "Billing"

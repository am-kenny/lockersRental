from django.http import HttpResponseNotFound
from django.shortcuts import render


def index(request):
    return None


def location(request, location_slug):
    return HttpResponseNotFound()


def available(request):
    return None


def closed(request):
    return None


def open(request):
    return None


def schedule(request):
    return None
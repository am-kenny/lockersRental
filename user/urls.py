from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='user_page'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('rented_lockers', views.rented_lockers, name='rented_lockers'),
    path('billing', views.billing, name='billing'),
    ]
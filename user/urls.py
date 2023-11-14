from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='user_page'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('register', views.register, name='register'),
    path('rented_lockers', views.rented_lockers, name='rented_lockers'),
    path('billing_address', views.billing_address, name='billing_address'),
    path('billing_address/delete/<int:billing_address_id>', views.delete_billing_address, name='delete_billing_address'),
    path('billing/delete/<int:billing_id>', views.delete_billing, name='delete_billing'),
    path('billing', views.billing, name='billing'),
    ]
import datetime

from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect

import locations.models
import rental.utils
from user.forms import RegisterForm, BillingAddressForm, BillingInfoForm


@login_required
def index(request):
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
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            return redirect("/")
        else:
            return HttpResponseNotFound("Failed to log in")

    return render(request, 'user/user_login.html', {})


@login_required
def user_logout(request):
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


@login_required
def billing_address(request):
    edit_address = request.GET.get('edit_address', None)
    edit_form = None

    if request.method == 'POST':
        form = BillingAddressForm(request.POST)
        if form.is_valid():
            form_data = form.save(commit=False)
            form_data.user_id = request.user.id
            if edit_address:
                form_data.id = int(edit_address)
            form_data.save()
            return redirect('billing_address')
    form = BillingAddressForm()
    user_addresses = request.user.userbillingaddress_set.all()

    if edit_address:
        edit_address = int(edit_address)
        edit_form = BillingAddressForm(instance=request.user.userbillingaddress_set.get(id=edit_address))

    return render(request, 'user/billing_address.html', {
        "user_addresses": user_addresses,
        "form": form,
        "edit_address": edit_address,
        "edit_form": edit_form
    })


@login_required
def delete_billing_address(request, billing_address_id):
    query = request.user.userbillingaddress_set.filter(id=billing_address_id)
    if query.exists():
        query.first().delete()

    return redirect('billing_address')


@login_required
def billing(request):
    edit_billing = request.GET.get('edit_billing', None)
    edit_form = None

    if request.method == 'POST':
        form = BillingInfoForm(request.POST)
        if form.is_valid():
            form_data = form.save(commit=False)
            form_data.user_id = request.user.id
            if edit_billing:
                form_data.id = int(edit_billing)
            form_data.save()
            return redirect('billing')
    form = BillingInfoForm()
    user_billings = request.user.userbillinginfo_set.all()

    if edit_billing:
        edit_billing = int(edit_billing)
        edit_form = BillingInfoForm(instance=request.user.userbillinginfo_set.get(id=edit_billing))

    return render(request, 'user/billing.html', {
        "user_billings": user_billings,
        "form": form,
        "edit_billing": edit_billing,
        "edit_form": edit_form
    })


@login_required
def delete_billing(request, billing_id):
    query = request.user.userbillinginfo_set.filter(id=billing_id)
    if query.exists():
        query.first().delete()

    return redirect('billing')


@login_required
def rented_lockers(request):
    # Get the search parameters
    location = request.GET.get('location', '')

    # Get all rentals for the current user
    all_rentals = locations.models.Rental.objects.filter(user=request.user)

    # Get unique Location objects
    all_locations = locations.models.Location.objects.filter(locker__rental__in=all_rentals).distinct()

    # If location is provided, filter by location
    if location:
        all_rentals = all_rentals.filter(locker__location=location)

    # Separate into current and past rentals
    current_rentals = all_rentals.filter(is_rented=True)
    for one_rental in current_rentals:
        one_rental.total_sum, one_rental.duration = rental.utils.calculate_rental_sum(one_rental.start_time,
                                                                                      datetime.datetime.now(),
                                                                                      one_rental.locker.locker_size.hourly_rate)

    past_rentals = all_rentals.filter(is_rented=False)

    return render(request, "user/user_rentals.html",
                  {"current_rentals": current_rentals, "past_rentals": past_rentals, "locations": all_locations})

import datetime

import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

import locations.models
from rental.utils import calculate_rental_sum


@login_required
def manage_rental(request, rental_id):
    rental = locations.models.Rental.objects.filter(id=rental_id, user=request.user, is_active=True).first()
    if not rental:
        return render(request, "not_found.html")
    return render(request, "rental/manage_rental.html", {"rental": rental})


@login_required
def close_locker(request, rental_id):
    rental = locations.models.Rental.objects.filter(id=rental_id, user=request.user, is_active=True).first()
    if not rental:
        return render(request, "not_found.html")
    try:
        response = requests.get(f"{rental.locker.location.API_URL}/close_locker/{rental.locker.locker_number}").json()
        locations.models.Locker.objects.filter(id=rental.locker.id).update(is_locked=response["isLocked"])
    except requests.exceptions.ConnectionError as err:
        print(err)
        return render(request, "connection_error.html", status=500)

    return redirect("rental", rental_id=rental_id)


@login_required
def open_locker(request, rental_id):
    rental = locations.models.Rental.objects.filter(id=rental_id, user=request.user, is_active=True).first()
    if not rental:
        return render(request, "not_found.html")
    try:
        response = requests.get(f"{rental.locker.location.API_URL}/open_locker/{rental.locker.locker_number}").json()
        locations.models.Locker.objects.filter(id=rental.locker_id).update(is_locked=response["isLocked"])
    except requests.exceptions.ConnectionError as err:
        print(err)

        return render(request, "connection_error.html", status=500)

    return redirect("rental", rental_id=rental_id)


@login_required
def end_rental(request, rental_id):
    rental_query = locations.models.Rental.objects.filter(id=rental_id, user=request.user, is_active=True)
    if not rental_query.exists():
        return render(request, "not_found.html")
    if rental_query.first().locker.is_locked:
        return redirect("rental", rental_id=rental_id)
    rental_query.update(end_time=datetime.datetime.now())
    rental = rental_query.first()
    total_sum, duration = calculate_rental_sum(rental.start_time,
                                               rental.end_time,
                                               rental.locker.locker_size.hourly_rate)

    rental_query.update(is_active=False,
                        total_sum=total_sum,
                        duration=duration)
    locations.models.Locker.objects.filter(id=rental.locker.id).update(is_available=True)

    return redirect("rented_lockers")

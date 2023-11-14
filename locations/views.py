import datetime

from django.shortcuts import render, redirect
import locations.models


def index(request):
    all_locations = locations.models.Location.objects.all()
    return render(request, "locations/index.html", {"locations": all_locations})


def location_page(request, location_slug):
    location_query = locations.models.Location.objects.filter(location_slug=location_slug)
    if not location_query.exists():
        return render(request, "not_found.html")
    location = location_query.first()
    locker_types = location.locker_set.filter(is_available=True).all().distinct("locker_size")
    return render(request, "locations/location.html", {"location": location, "locker_types": locker_types})


def select_locker(request, location_slug, locker_size_id):
    location_query = locations.models.Location.objects.filter(location_slug=location_slug)
    location = location_query.first()
    if not location_query.exists():
        return render(request, "not_found.html")
    try:
        locker_size = locations.models.LockerSize.objects.get(id=locker_size_id)
    except locations.models.LockerSize.DoesNotExist:
        return render(request, "not_found.html")

    locker_query = location.locker_set.filter(locker_size=locker_size, is_available=True)
    is_available = locker_query.exists()
    error = None

    if request.method == 'POST' and is_available:
        if not request.user.userbillinginfo_set.exists():
            error = "You need to add billing info first"
        else:
            locker_to_rent = locker_query.first()
            rental = locations.models.Rental.objects.create(locker=locker_to_rent,
                                                            user=request.user,
                                                            start_time=datetime.datetime.now())
            locations.models.Locker.objects.filter(id=locker_to_rent.id).update(is_available=False)

            return redirect("rental", rental_id=rental.id)

    return render(request, "locations/locker_selection.html", {
        "location": location,
        "locker_size": locker_size,
        "is_available": is_available,

        "error": error}, status=200)

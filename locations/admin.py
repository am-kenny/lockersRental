from django.contrib import admin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import path, reverse
from django.utils.html import format_html
from django.views.generic import DetailView
from django.contrib.admin.views.decorators import staff_member_required
import requests

from locations import models

admin.site.register(models.Address)
admin.site.register(models.LockerSize)
admin.site.register(models.Locker)
admin.site.register(models.Rental)


@staff_member_required
def sync_location_lockers(request, pk):
    location = get_object_or_404(models.Location, id=pk)
    response = requests.get(f"{location.API_URL}/get_all_lockers")
    if response.status_code == 200:
        lockers = response.json()
        for locker in lockers:
            size = models.LockerSize.objects.get(id=locker["locker_size"])
            locker_query = models.Locker.objects.filter(locker_number=locker["locker_number"], location=location)
            if locker_query.exists():
                locker_query.update(
                    locker_size=size,
                    location=location,
                )
            else:
                models.Locker.objects.create(
                    locker_size=size,
                    location=location,
                    locker_number=locker["locker_number"],
                    is_available=True
                )
        return redirect("admin:location_lockers", pk=pk)
    return HttpResponse(status=500)


class LocationDetailView(PermissionRequiredMixin, DetailView):
    permission_required = "locations.change_locker"
    template_name = "locations/admin_location.html"
    model = models.Location

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            **admin.site.each_context(self.request),
            "opts": self.model._meta,
        }


@admin.register(models.Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("location_name", "is_active", "location_lockers")

    def get_urls(self):
        return [
            path(
                "<pk>/lockers",
                self.admin_site.admin_view(LocationDetailView.as_view()),
                name="location_lockers",
            ),
            path(
                "<pk>/sync_lockers",
                sync_location_lockers,
                name="sync_location_lockers",
            ),

            *super().get_urls(),
        ]

    def location_lockers(self, obj: models.Location) -> str:
        url = reverse("admin:location_lockers", args=[obj.pk])
        return format_html(f'<a href="{url}">Location lockers</a>')
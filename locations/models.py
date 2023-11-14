from django.contrib.auth.models import User
from django.db import models


class Address(models.Model):
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    house_number = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.zip_code}"


class Location(models.Model):
    location_name = models.CharField(max_length=255)
    location_slug = models.CharField(max_length=255, unique=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    API_URL = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.location_name} ({self.location_slug})"


class LockerSize(models.Model):
    width = models.IntegerField()
    height = models.IntegerField()
    depth = models.IntegerField()
    hourly_rate = models.DecimalField(max_digits=5, decimal_places=2)
    size_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.size_name} ({self.width}x{self.height}x{self.depth})"


class Locker(models.Model):
    locker_size = models.ForeignKey(LockerSize, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    locker_number = models.IntegerField()
    is_available = models.BooleanField(default=True)
    is_locked = models.BooleanField(default=False)

    def __str__(self):
        return f"Locker #{self.locker_number} ({self.locker_size.size_name})"


class Rental(models.Model):
    locker = models.ForeignKey(Locker, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    is_rented = models.BooleanField(default=True)

    def __str__(self):
        return f"Locker #{self.locker.locker_number} ({self.locker.locker_size.size_name})"
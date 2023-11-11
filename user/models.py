from django.contrib.auth.models import User
from django.db import models


class UserBillingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    house_number = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.zip_code}"


class UserBillingInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16)
    expiration_year = models.IntegerField()
    expiration_month = models.IntegerField()
    cvv = models.CharField(max_length=3)
    billing_address = models.ForeignKey(UserBillingAddress, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.card_number} ({self.user.username})"
from django.contrib import admin

from user import models


admin.site.register(models.UserBillingAddress)
admin.site.register(models.UserBillingInfo)

from django.urls import path

from . import views

urlpatterns = [
    path('<rental_id>', views.manage_rental, name='rental'),
    path('<rental_id>/end', views.end_rental, name='end_rental'),
    path('<rental_id>/close', views.close_locker, name='close_locker'),
    path('<rental_id>/open', views.open_locker, name='open_locker'),
]

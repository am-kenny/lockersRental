from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='locations'),
    path('<location_slug>', views.location_page, name='location'),
    path('<location_slug>/selection/<locker_size_id>', views.select_locker, name='locker_selection'),
]

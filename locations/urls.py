from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='locations'),
    path('<location_slug>', views.location_page, name='location'),
    path('<location_slug>/available', views.available, name='available'),
    path('<location_slug>/close', views.close_locker, name='close'),
    path('<location_slug>/open', views.open_locker, name='open'),
    path('<location_slug>/selection/<locker_size_id>', views.select_locker, name='locker_selection'),
]

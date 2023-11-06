from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='locations'),
    path('<location_slug>', views.location, name='location'),
    path('<location_slug>/available', views.available, name='available'),
    path('<location_slug>/close', views.closed, name='close'),
    path('<location_slug>/open', views.open, name='open'),
    path('<location_slug>/selection', views.schedule, name='selection'),
]

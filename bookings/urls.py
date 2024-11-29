# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('time-slots/<slug:community_centre_slug>/', views.time_slot_view, name='time_slots'),
    path('booking/<slug:community_centre_slug>/<int:time_slot_id>/', views.create_booking_view, name='booking-details'),
]

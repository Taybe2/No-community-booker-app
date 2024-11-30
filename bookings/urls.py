# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('time-slots/', views.time_slot_view, name='time_slots'),
    path('booking/<int:time_slot_id>/', views.create_booking_view, name='booking-details'),
    path('my-bookings/', views.my_bookings_view, name='my-bookings'),
    path('booking/cancel/<slug:slug>/', views.cancel_booking, name='cancel-booking'),
    path('bookings/<slug:slug>/edit/', views.edit_booking, name='edit-booking'),
]

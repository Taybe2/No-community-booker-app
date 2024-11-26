from django.urls import path
from .views import generate_time_slots_view

urlpatterns = [
    path(
        'generate-time-slots/<int:centre_id>/',
        generate_time_slots_view,
        name='generate_time_slots',
    ),
]

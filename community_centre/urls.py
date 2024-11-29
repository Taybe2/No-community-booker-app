from django.urls import path
from . import views

urlpatterns = [
    path(
        'generate-time-slots/<int:centre_id>/',
        views.generate_time_slots_view,
        name='generate_time_slots',
    ),
    path('', views.home_page, name='home'),
]

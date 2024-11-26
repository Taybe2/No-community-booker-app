# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('time-slots/', views.time_slot_view, name='time_slot_view'),
]

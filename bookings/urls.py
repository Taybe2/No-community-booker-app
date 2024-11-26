from django.urls import path
from . import views

urlpatterns = [
    path('time-slots/', views.TimeSlotListView.as_view(), name='time_slot_list'),
]

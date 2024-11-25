from django.db import models
from django.contrib.auth.models import User
from community_centre.models import CommunityCentre

# Create your models here.
class TimeSlot(models.Model):
    community_centre = models.ForeignKey(
        'community_centre.CommunityCentre', on_delete=models.CASCADE, related_name='time_slots'
    )
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('community_centre', 'date', 'start_time')

    def __str__(self):
        return f"{self.date} {self.start_time} - {self.end_time}"


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    time_slot = models.ForeignKey('TimeSlot', on_delete=models.CASCADE, related_name='bookings')
    community_centre = models.ForeignKey(
        'community_centre.CommunityCentre', on_delete=models.CASCADE, related_name='bookings'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking by {self.user.username} for {self.time_slot} at {self.community_centre.name}"

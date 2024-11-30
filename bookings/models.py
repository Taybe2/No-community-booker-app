from django.db import models
from django.utils.text import slugify
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
        ordering = ["date", "start_time"]

    def __str__(self):
        return f"{self.date} {self.start_time} - {self.end_time}"


class Booking(models.Model):
    OCCASION_TYPE_CHOICES = [
        ('private', 'Private'),
        ('public', 'Public'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    time_slot = models.OneToOneField('TimeSlot', on_delete=models.CASCADE, related_name='booking')
    community_centre = models.ForeignKey(
        'community_centre.CommunityCentre', on_delete=models.CASCADE, related_name='bookings'
    )
    occasion = models.CharField(max_length=100, default='')
    slug = models.SlugField(unique=True, blank=True, null=True, max_length=100)
    occasion_type = models.CharField(
        max_length=10,
        choices=OCCASION_TYPE_CHOICES,
        default='private'
    )  # Choice field for type (Private/Public)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Example: "user123-2024-12-01-14-00"
        unique_identifier = f"{self.user.username}-{self.occasion}-{self.time_slot.date}-{self.time_slot.start_time}"
        self.slug = slugify(unique_identifier)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Booking by {self.user.username} for {self.time_slot} at {self.community_centre.name}"

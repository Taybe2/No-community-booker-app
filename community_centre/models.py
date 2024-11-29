from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
# Days of the week as integers
DAYS_OF_WEEK = [
    (1, 'Monday'),
    (2, 'Tuesday'),
    (3, 'Wednesday'),
    (4, 'Thursday'),
    (5, 'Friday'),
    (6, 'Saturday'),
    (7, 'Sunday'),
]

class CommunityCentre(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    address = models.CharField(max_length=100)
    operating_start_day = models.IntegerField(choices=DAYS_OF_WEEK)
    operating_end_day = models.IntegerField(choices=DAYS_OF_WEEK)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:  # Generate slug only if it's not set
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

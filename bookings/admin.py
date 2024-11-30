from django.contrib import admin
from django.utils.text import slugify
from .models import Booking, TimeSlot

# Register your models here.

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'community_centre', 'time_slot', 'created_at')
    list_filter = ('community_centre', 'time_slot__date')
    search_fields = ('user__username', 'community_centre__name')
    readonly_fields = ('slug',)

    def save_model(self, request, obj, form, change):
        # Generate slug only if it doesn't already exist
        if not obj.slug:
            unique_identifier = f"{obj.user.username}-{obj.time_slot.date}-{obj.time_slot.start_time}-{obj.occasion}"
            obj.slug = slugify(unique_identifier)
        
        # Call the default save logic to save the object
        super().save_model(request, obj, form, change)

@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('community_centre', 'date', 'start_time', 'end_time', 'created_at')  # Customize the columns displayed
    list_filter = ('community_centre', 'date')  # Add filters for admin
    search_fields = ('community_centre__name', 'date')  # Enable search by community center name and date
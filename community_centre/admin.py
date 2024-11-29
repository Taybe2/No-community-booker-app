from django.utils.html import format_html
from django.urls import reverse
from django.contrib import admin
from .models import CommunityCentre

@admin.register(CommunityCentre)
class CommunityCentreAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'updated_at', 'generate_time_slots_button')
    prepopulated_fields = {'slug': ('name',)}

    def generate_time_slots_button(self, obj):
        """Display a button in the admin to go to the custom time slots view."""
        url = reverse('generate_time_slots', args=[obj.pk])
        return format_html('<a class="button" href="{}">Generate Time Slots</a>', url)
    
    generate_time_slots_button.short_description = "Generate Time Slots"

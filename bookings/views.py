from datetime import datetime, timedelta
from django.views.generic import ListView
from .models import TimeSlot

class TimeSlotListView(ListView):
    model = TimeSlot
    template_name = 'bookings/timeslot_list.html'  # Specify the template to use
    context_object_name = 'time_slots'  # The variable name for the object list in the template
    paginate_by = 14  # Number of time slots per page

    def get_queryset(self):
        """Return time slots that are scheduled from tomorrow onward."""
        today = datetime.now().date()  # Get today's date
        tomorrow = today + timedelta(days=1)  # Get tomorrow's date
        # Filter time slots for dates starting from tomorrow
        return TimeSlot.objects.filter(date__gte=tomorrow).order_by('date', 'start_time')
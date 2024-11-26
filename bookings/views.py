from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from .models import TimeSlot

def time_slot_view(request):
    """Display time slots for the current week (starting today) or other weeks (starting Monday)."""
    today = timezone.now().date()  # Get today's date

    # Get the week offset from the URL parameters (default is 0)
    week_offset = int(request.GET.get('week_offset', 0))  # 0 for the current week, +1 for next week, -1 for previous week

    # if week_offset == 0:
    #     # Current week starts from today
    #     week_start = today
    # else:
    #     # Other weeks always start from Monday
    week_start = today - timedelta(days=today.weekday()) + timedelta(weeks=week_offset)
    print(week_start)
    # Calculate the end of the week (Sunday)
    week_end = week_start + timedelta(days=6)  # End of the week (Sunday)

    # Fetch all time slots between week_start and week_end
    time_slots = TimeSlot.objects.filter(date__range=[week_start, week_end]).order_by('date', 'start_time')

    # Group time slots by day
    slots_by_day = {}
    for day in (week_start + timedelta(days=i) for i in range((week_end - week_start).days + 1)):  # Iterate through week_start to week_end
        slots_by_day[day] = time_slots.filter(date=day)  # Fetch time slots for each day, even if empty

    # Prepare the context
    context = {
        'slots_by_day': slots_by_day,  # A dictionary of dates and their slots
        'week_start': week_start,  # Start of the current/selected week
        'week_end': week_end,  # End of the current/selected week
        'week_offset': week_offset,  # Offset for next/previous week navigation
        'today': today,  # Pass today's date to the template for comparison
    }

    return render(request, 'bookings/timeslot_list.html', context)

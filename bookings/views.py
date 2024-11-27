from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from .models import TimeSlot

def time_slot_view(request):
    """Display time slots for the current week or other weeks, with all days accounted for."""
    today = timezone.now().date()  # Get today's date

    # Get the week offset from the URL parameters (default is 0)
    week_offset = int(request.GET.get('week_offset', 0))  # 0 for the current week, +1 for next week, -1 for previous week

    # if week_offset == 0:
    #     # Current week starts from today
    #     week_start = today
    # else:
    #     # Other weeks always start from Monday
    week_start = today - timedelta(days=today.weekday()) + timedelta(weeks=week_offset)

    # Calculate the end of the week (Sunday)
    week_end = week_start + timedelta(days=6)  # End of the week (Sunday)

    # Fetch all time slots between week_start and week_end
    time_slots = TimeSlot.objects.filter(date__range=[week_start, week_end]).order_by('date', 'start_time')

    # Group time slots by day
    slots_by_day = {}
    current_day = week_start
    while current_day <= week_end:
        slots_for_day = time_slots.filter(date=current_day)
        slots_with_bookings = []
        time_slot = TimeSlot.objects.first()

        # Check each time slot for bookings
        for slot in slots_for_day:
            try:
                # Try to access the related 'booking'
                slot.booking  # If no booking exists, this will raise RelatedObjectDoesNotExist
                has_booking = True
            except:
                has_booking = False
            slots_with_bookings.append({
                'slot': slot,
                'has_booking': has_booking
            })

        slots_by_day[current_day] = slots_with_bookings
        current_day += timedelta(days=1)

    # Prepare the context
    context = {
        'slots_by_day': slots_by_day,  # A dictionary of dates and their slots with booking info
        'week_start': week_start,  # Start of the current/selected week
        'week_end': week_end,  # End of the current/selected week
        'week_offset': week_offset,  # Offset for next/previous week navigation
        'today': today,  # Pass today's date to the template for comparison
    }

    return render(request, 'bookings/timeslot_list.html', context)

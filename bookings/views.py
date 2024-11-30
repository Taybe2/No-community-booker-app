from datetime import timedelta
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.utils.text import slugify
from community_centre.models import CommunityCentre
from .models import TimeSlot, Booking
from .forms import BookingForm

community_centre = CommunityCentre.objects.first()

def time_slot_view(request):
    """Display time slots for the current week or other weeks, with all days accounted for."""

    today = timezone.now().date()  # Get today's date

    # Get the week offset from the URL parameters (default is 0)
    week_offset = int(request.GET.get('week_offset', 0))  # 0 for the current week, +1 for next week, -1 for previous week

    # Weeks always start from Monday
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
    
    # Handle form submission (time slot selection)
    if request.method == 'POST':
        selected_slot_id = request.POST.get('time_slot')
        if selected_slot_id:
            # Save the booking in the database or perform other actions
            return redirect('booking-details', time_slot_id=selected_slot_id)
    
    context = {
        'slots_by_day': slots_by_day,
        'week_start': week_start,
        'week_end': week_end,
        'week_offset': week_offset,
        'today': today,
    }

    return render(request, 'bookings/timeslot_list.html', context)

@login_required
def create_booking_view(request, time_slot_id):
    """Handle booking creation for a selected time slot."""
    time_slot = get_object_or_404(TimeSlot, id=time_slot_id)

    # Check if the time slot is already booked
    if Booking.objects.filter(time_slot=time_slot).exists():
        return render(request, 'bookings/booking_error.html', {
            'message': 'This time slot is already booked.'
        })

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # Associate the booking with the logged-in user
            booking.time_slot = time_slot
            booking.community_centre = community_centre
            booking.save()
            return redirect('my-bookings')  # Redirect to My Bookings page

    else:
        form = BookingForm(initial={'time_slot': time_slot})

    return render(request, 'bookings/create_booking.html', {
        'form': form,
        'time_slot': time_slot,
    })

@login_required
def my_bookings_view(request):
    """Display the user's bookings and allow editing or cancellation."""
    # Get the current user
    user = request.user

    # Fetch the bookings made by the logged-in user
    bookings = Booking.objects.filter(user=user).order_by('-created_at')  # You can order by booking creation date

    context = {
        'bookings': bookings,
    }

    return render(request, 'bookings/my_bookings.html', context)

@login_required
def cancel_booking(request, slug):
    """Cancel an existing booking."""
    # Get the booking object by ID
    booking = get_object_or_404(Booking, slug=slug, user=request.user)

    # Ensure that the booking is not in the past (optional)
    if booking.time_slot.date < timezone.now().date():
        return render(request, 'bookings/booking_error.html', {
            'message': 'You cannot cancel bookings in the past.'
        })

    # Cancel the booking (delete it)
    booking.delete()

    return redirect('my-bookings')  # Redirect to the user's bookings page

@login_required
def edit_booking(request, slug):
    """Edit an existing booking."""
    booking = get_object_or_404(Booking, slug=slug, user=request.user)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()  # Save the updated booking
            return redirect('my-bookings')
    else:
        form = BookingForm(instance=booking)

    return render(request, 'bookings/edit_booking.html', {
        'form': form,
        'booking': booking
    })
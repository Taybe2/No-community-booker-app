from datetime import timedelta, datetime
from bookings.models import TimeSlot

def generate_time_slots(community_centre, start_date, end_date, slot_duration_minutes=60):
    """
    Generate time slots for a community center between a start and end date.
    
    :param community_centre: The community center for which to generate time slots
    :param start_date: The start date for generating time slots
    :param end_date: The end date for generating time slots
    :param slot_duration_minutes: The duration of each time slot in minutes (default is 60 minutes)
    """
    # Get the operating days and opening/closing times for the community center
    operating_days = range(community_centre.operating_start_day - 1, community_centre.operating_end_day)
    opening_time = community_centre.opening_time
    closing_time = community_centre.closing_time

    current_date = start_date
    while current_date <= end_date:
        # Check if the current date is an operating day
        if current_date.weekday() in operating_days:
            # Initialize the start_time and end_time for the current day
            start_time = datetime.combine(current_date, opening_time)
            end_time = datetime.combine(current_date, closing_time)
            
            # Create time slots if they do not already exist
            while start_time + timedelta(minutes=slot_duration_minutes) <= end_time:
                # Check if the time slot already exists
                if not TimeSlot.objects.filter(
                    community_centre=community_centre,
                    date=current_date,
                    start_time=start_time.time(),
                ).exists():
                    TimeSlot.objects.create(
                        community_centre=community_centre,
                        date=current_date,
                        start_time=start_time.time(),
                        end_time=(start_time + timedelta(minutes=slot_duration_minutes)).time()
                    )
                # Move to the next time slot
                start_time += timedelta(minutes=slot_duration_minutes)
        
        # Move to the next day
        current_date += timedelta(days=1)

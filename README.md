# README for Community Centre Booking App

## Project Overview
The **Community Centre Booking App** allows users to view available time slots, book slots for events, and manage their bookings. Designed for simplicity and efficiency, this app ensures seamless scheduling for community centers.

## Features
1. **Explore Available Time Slots**
  - Users can browse available and booked time slots for the current or upcoming weeks.
  - Booked slots are marked, and available slots can be reserved.
2. **User Registration and Login**
  - Users must create an account or log in to book time slots and manage their bookings.
3. **Booking Management**
  - Logged-in users can view their current and past bookings.
  - Bookings can be canceled or rescheduled.
4. **Admin Functionality**
  - Admins can manage time slots and view all bookings.

## Page Flow
This app follows a user-friendly navigation structure:

### Homepage (/)
- Introduces the app with a simple interface.
- Features a "See Available Times" button, leading users to browse available time slots.

### Available Time Slots Page (/time-slots/)
- Displays all time slots for the current week.
- Users can navigate to previous or next weeks using navigation buttons.
- **Behavior:**
  - Non-logged-in users clicking "Book Now" are redirected to the Login Page.
  - Logged-in users can proceed to the Booking Confirmation Page.

### Booking Confirmation Page (/bookings/confirm/)
- Allows users to finalize their booking by specifying:
  - Occasion name (e.g., Birthday Party).
  - Occasion type (Private or Public).
- Users confirm the booking, and the time slot is marked as booked.

### My bookings Page (/my-bookings/)
- Displays a personalized dashboard showing:
  - Current and past bookings.
  - Options to cancel or reschedule bookings.

### Login Page (/login/)
- Allows users to log in to access restricted features.
- Redirects to the previously visited page or the homepage.

### Register Page (/register/)
- Enables users to create an account to start booking time slots.

## How to Use
1. **For General Users:**
  - Visit the app homepage and browse available time slots.
  - Log in or register to book a time slot.
  - View and manage bookings from the My Bookings page.
2. **For Admins:**
  - Manage time slots and bookings via the Django admin panel.

## Tech Stack

## Setup Instructions

## Future Enchancements
- Add payment integration for bookings
- Implement recurring bookings for regular events.
- Support multiple spaces booking management for the community centres




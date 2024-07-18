from .models import Booking


def booking_exists(request):
    """
    Checks if a logged in guest has made a booking
    """
    if request.user.is_authenticated:
        has_booking = Booking.objects.filter(user=request.user).exists()
    else:
        has_booking = False

    return {
        'booking_exists': has_booking
    }

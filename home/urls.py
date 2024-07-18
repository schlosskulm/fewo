from django.urls import path
from . import views


urlpatterns = [
    path('your-bookings/', views.BookingList.as_view(), name='your-bookings'),
    path('all-bookings/', views.AllBookingsList.as_view(),
         name='all-bookings'),
    path('cancel_booking/<int:booking_id>', views.cancel_booking,
         name='cancel_booking'),
    path('confirm_booking/<int:booking_id>', views.confirm_booking,
         name='confirm_booking'),
    path('delete_booking/<int:booking_id>', views.delete_booking,
         name='delete_booking'),
]

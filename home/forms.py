from bootstrap_datepicker_plus.widgets import DatePickerInput
from django.forms import forms, ModelForm
from django import forms
from .models import Booking, Contact
from django.db import models
import datetime


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['first_name', 'last_name', 'birth_date', 'email',
                  'phone_number', 'address', 'zip_code', 'city', 'country',
                  'booking_item', 'arrival_date', 'departure_date',
                  'amount_guests', 'nationality', 'passport_number', 'animals',
                  'message']
        exclude = ['booking_date', 'booking_status']
        widgets = {
            "birth_date": DatePickerInput(options={"format": "DD/MM/YYYY"}),
            "arrival_date": DatePickerInput(),
            "departure_date": DatePickerInput(range_from="arrival_date"),
        }

    def clean(self):
        """
        Date Validation
        """
        cleaned_data = super().clean()
        arrival_date = cleaned_data.get("arrival_date")
        departure_date = cleaned_data.get("departure_date")
        birth_date = cleaned_data.get("birth_date")

        if birth_date is not None:
            if birth_date > datetime.date.today():
                raise forms.ValidationError(
                    "Your birth date cannot be in the future!")
            elif departure_date is not None and arrival_date is not None:
                if departure_date == arrival_date:
                    raise forms.ValidationError(
                        """Your arrival date cannot be the same day as your
                        departure date!""")
                elif arrival_date is not None:
                    if arrival_date < datetime.date.today():
                        raise forms.ValidationError(
                            "Your booking date cannot be in the past!")
                    elif departure_date is not None:
                        if departure_date < datetime.date.today():
                            raise forms.ValidationError(
                                "Your booking date cannot be in the past!")


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'mail', 'inquiry']
        labels = {
            "name":  "Your Name",
            "mail": "E-Mail",
            "inquiry": "Message",
        }

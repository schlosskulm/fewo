from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now
from django.utils import timezone, dateformat
from django.forms import forms
import datetime
import re

# Booking model

class Booking(models.Model):
    """
    Saves guests' booking information made via the form to database
    """
    user = models.ForeignKey(User, on_delete=models.RESTRICT,
                             related_name="user_name", default='1')
    booking_date = models.DateTimeField(default=now)
    status = (
        ('Angefragt', 'Angefragt'),
        ('Bestätigt', 'Bestätigt'),
        ('Storniert', 'Storniert'),
    )
    booking_status = models.CharField(choices=status, blank=True, null=True,
                                      max_length=100, default='Angefragt')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    email = models.EmailField(max_length=100)
    phone_number = models.BigIntegerField()
    address = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    booking_object = (
        ('Obere Ferienwohnung', 'Obere Ferienwohnung'),
        ('Untere Ferienwohnung', 'Untere Ferienwohnung'),
        ('Gesamtes Haus', 'Gesamtes Haus'),
    )
    booking_item = models.CharField(choices=booking_object, max_length=100)
    arrival_date = models.DateField()
    departure_date = models.DateField()
    guest_number = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
        ('15', '15'),
    )
    amount_guests = models.CharField(choices=guest_number, max_length=100)
    guest_nationality = (
        ('Deutsch', 'Deutsch'),
        ('Andere / Other', 'Andere / Other'),
    )
    nationality = models.CharField(choices=guest_nationality, max_length=100)
    passport_number = models.CharField(max_length=100, blank=True, null=True)
    animals = models.BooleanField(blank=True, null=True)
    message = models.TextField(max_length=4000)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f"""Buchung Nr. {self.id}: {self.last_name}, {self.first_name}
        (gebucht am {self.booking_date})"""


class Contact(models.Model):
    """
    Contact form model
    """
    request_date = models.DateTimeField(default=now)
    name = models.CharField(max_length=100)
    mail = models.EmailField(max_length=100)
    inquiry = models.TextField(max_length=4000)

    def __str__(self):
        return f'Nr. {self.id}: Neue Nachricht von {self.name}'
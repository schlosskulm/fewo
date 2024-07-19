from django.contrib import messages
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
import requests

from .models import Booking, Contact
from .forms import BookingForm, ContactForm

# Booking Form

def buchung_seite(request):
    """
    Posts entered booking form data to database
    and displays confirmation message
    """

    if request.method == "POST":
        form = BookingForm(data=request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.add_message(request, messages.SUCCESS, """Danke für
            deine Buchungsanfrage. Wir melden uns baldmöglichst bei dir zurück.""")
            return redirect("start-seite")
    else:
        form = BookingForm()

    return render(
        request,
        "home/buchung.html",
        {
            "form": form
        },
    )


def check_if_booking_exists(request):
    """
    Checks if a logged in guest has made a booking
    """
    current_user = request.user
    if current_user.is_authenticated:
        booking_exists = Booking.objects.filter(user=current_user).exists()
    else:
        booking_exists = False

    return {
        "current_user": current_user,
        "booking_exists": booking_exists
    }


# Your Bookings View

class BookingList(generic.ListView):
    """
    Displays booking details of current
    logged in user on your-bookings page
    """

    model = Booking
    template_name = "home/deine-buchungen.html"

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Booking.objects.filter(user=self.request.user)


# All Bookings View
class AllBookingsList(generic.ListView):
    """
    View for hosts that displays all bookings guests have made
    """

    model = Booking
    queryset = Booking.objects.all()
    template_name = "home/alle-buchungen.html"


# Confirm Booking View

def confirm_booking(request, booking_id):
    """
    Functionality for hosts to confirm a booking
    """
    booking = get_object_or_404(Booking, pk=booking_id)

    if not request.user.is_anonymous:
        booking.booking_status = "Bestätigt"
        booking.save()
        messages.add_message(request, messages.SUCCESS, f"""Buchung
        Nr. {booking_id} wurde bestätigt!""")
    else:
        messages.add_message(request, messages.ERROR, """Es gab leider ein
        Problem bei deiner Buchung.""")

    return HttpResponseRedirect(reverse("alle-buchungen"))


# Cancel Booking View

def cancel_booking(request, booking_id):
    """
    Functionality for guests and hosts to cancel a booking
    """
    booking = get_object_or_404(Booking, pk=booking_id)

    if not request.user.is_anonymous:
        booking.booking_status = "Storniert"
        booking.save()
        messages.add_message(request, messages.SUCCESS, f"""Buchung
        Nr. {booking_id} wurde storniert!""")
    else:
        messages.add_message(request, messages.ERROR, """Es gab einen
        Fehler beim Versuch die Buchung zu stornieren.""")

    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse("deine-buchungen"))
    elif request.user.is_superuser:
        return HttpResponseRedirect(reverse("alle-buchungen"))


# Delete Booking View

def delete_booking(request, booking_id):
    """
    Functionality for hosts to delete a booking
    """
    booking = get_object_or_404(Booking, pk=booking_id)

    if not request.user.is_anonymous:
        booking.delete()
        messages.add_message(request, messages.SUCCESS, f"""Buchung
        Nr. {booking_id} wurde gelöscht!""")
    else:
        messages.add_message(request, messages.ERROR, """Es gab einen
        Fehler beim Versuch, die Buchung zu löschen.""")

    return HttpResponseRedirect(reverse("alle-buchungen"))


# Contact View

def kontakt_seite(request):
    """
    Posts guest messages made via contact form to database
    """
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(request, messages.SUCCESS, """Danke für deine
            Nachricht. Wir melden uns baldmöglichst bei dir zurück.""")
            return redirect("start-seite")
        else:
            messages.add_message(request, messages.ERROR, """Es gab einen
            Fehler beim Versuch, die Nachricht abzuschicken.""")
    else:
        contact_form = ContactForm()

    return render(
        request,
        "home/kontakt.html",
        {
            "contact_form": contact_form
        },
    )


# Template Views - Render HTML pages

def agb_seite(request):
    return render(request, "home/agb.html")


def alle_buchungen_seite(request):
    return render(request, "home/alle-buchungen.html")


def anfahrt_seite(request):
    return render(request, "home/anfahrt.html")


def datenschutz_seite(request):
    return render(request, "home/datenschutz.html")


def ferienwohnung_oben_seite(request):
    return render(request, "home/ferienwohnung-oben.html")


def ferienwohnung_unten_seite(request):
    return render(request, "home/ferienwohnung-unten.html")


def galerie_seite(request):
    return render(request, "home/galerie.html")


def haus_seite(request):
    return render(request, "home/haus-mieten.html")


def hausregeln_seite(request):
    return render(request, "home/hausregeln.html")


def impressum_seite(request):
    return render(request, "home/impressum.html")


def initiativen_seite(request):
    return render(request, "home/initiativen.html")


def projektarchiv_seite(request):
    return render(request, "home/projektarchiv.html")


def start_seite(request):
    return render(request, "home/index.html")


def tagesausflug_seite(request):
    return render(request, "home/tagesausflug.html")


def ueber_uns_seite(request):
    return render(request, "home/ueber-uns.html")


def deine_buchungen_seite(request):
    return render(request, "home/deine-buchungen.html")

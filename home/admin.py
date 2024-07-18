from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from home.models import Booking, Contact


@admin.register(Booking)
class PostAdmin(SummernoteModelAdmin):
    search_fields = ['first_name', 'last_name', 'email', 'city']
    list_filter = ['booking_date']


# Register your models here.
admin.site.register(Contact)

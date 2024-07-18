from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.main_page, name='main-page'),
    path('about-us/', views.about_us_page, name='about-us'),
    path('accounts', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('booking/', views.booking_page, name='booking'),
    path('contact/', views.contact_page, name='contact'),
    path('house/', views.house_page, name='house'),
    path('house/house-rules/', views.house_rules_page, name='house-rules'),
    path('house/lower-apartment/', views.lower_apartment_page,
         name='lower-apartment'),
    path('house/upper-apartment/', views.upper_apartment_page,
         name='upper-apartment'),
    path('schlosskulm/day-trips/', views.day_trips_page, name='day-trips'),
    path('schlosskulm/location/', views.location_page, name='location'),
    path('schlosskulm/gallery/', views.gallery_page, name='gallery'),
    path('summernote', include('django_summernote.urls')),
    path('booking/', include("home.urls"), name="home-urls"),
]

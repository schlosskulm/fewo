from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.start_seite, name='start-seite'),
    path('ueber-uns/', views.ueber_uns_seite, name='ueber-uns'),
    path('accounts', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('buchung/', views.buchung_seite, name='buchung'),
    path('kontakt/', views.kontakt_seite, name='kontakt'),
    path('haus/haus-mieten/', views.haus_seite, name='haus-mieten'),
    path('haus/hausregeln/', views.hausregeln_seite, name='hausregeln'),
    path('haus/ferienwohnung-unten/', views.ferienwohnung_unten_seite,
         name='ferienwohnung-unten'),
    path('haus/ferienwohnung-oben/', views.ferienwohnung_oben_seite,
         name='ferienwohnung-oben'),
    path('schlosskulm/tagesausflug/', views.tagesausflug_seite, name='tagesausflug'),
    path('schlosskulm/anfahrt/', views.anfahrt_seite, name='anfahrt'),
    path('schlosskulm/galerie/', views.galerie_seite, name='galerie'),
    path('summernote', include('django_summernote.urls')),
    path('buchung/', include('home.urls'), name='home-urls'),
]

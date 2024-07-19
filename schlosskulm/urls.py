from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.start_seite, name='start-seite'),
    path('accounts', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('rechtliches/agb', views.agb_seite, name='agb'),
    path('buchung/', views.buchung_seite, name='buchung'),
    path('buchung/', include('home.urls'), name='home-urls'),
    path('rechtliches/datenschutz', views.datenschutz_seite, name='datenschutz'),
    path('haus/haus-mieten/', views.haus_seite, name='haus-mieten'),
    path('haus/hausregeln/', views.hausregeln_seite, name='hausregeln'),
    path('haus/ferienwohnung-unten/', views.ferienwohnung_unten_seite,
         name='ferienwohnung-unten'),
    path('haus/ferienwohnung-oben/', views.ferienwohnung_oben_seite,
         name='ferienwohnung-oben'),
    path('schlosskulm/initiativen/', views.initiativen_seite, name='initiativen'),
    path('projektarchiv/', views.projektarchiv_seite, name='projektarchiv'),
    path('rechtliches/impressum', views.impressum_seite, name='impressum'),
    path('kontakt/', views.kontakt_seite, name='kontakt'),
    path('schlosskulm/tagesausflug/', views.tagesausflug_seite, name='tagesausflug'),
    path('schlosskulm/anfahrt/', views.anfahrt_seite, name='anfahrt'),
    path('schlosskulm/galerie/', views.galerie_seite, name='galerie'),
    path('summernote', include('django_summernote.urls')),
    path('ueber-uns/', views.ueber_uns_seite, name='ueber-uns'),
]

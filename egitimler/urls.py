from django.urls import path
from . import views

app_name = 'egitimler' # Bu isim alanı önemli! Link verirken kullanacağız.

urlpatterns = [
    path('egitim/<slug:slug>/', views.egitim_detay, name='detay'),
    path('egitimler/tumu/', views.tum_egitimler, name='liste'),
]
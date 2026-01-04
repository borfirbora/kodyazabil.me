from django.urls import path
from . import views

urlpatterns = [
    # Tırnakların arası boş, yani 'ana sayfa'
    path('', views.anasayfa, name='anasayfa'),
]
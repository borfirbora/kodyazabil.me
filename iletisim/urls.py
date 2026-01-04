from django.urls import path
from . import views

app_name = 'iletisim'

urlpatterns = [
    path('', views.iletisim_sayfasi, name='sayfa'),
]
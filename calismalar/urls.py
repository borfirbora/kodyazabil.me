from django.urls import path
from . import views

app_name = 'calismalar'

urlpatterns = [
    path('', views.tum_projeler, name='liste'),
]
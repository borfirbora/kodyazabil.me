from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_liste, name='liste'),
    path('<slug:slug>/', views.blog_detay, name='detay'),
]
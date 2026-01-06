from django.urls import path
from . import views
from .feeds import SonYazilarFeed

app_name = 'blog'

urlpatterns = [
    path('', views.blog_liste, name='liste'),
    path('<slug:slug>/', views.blog_detay, name='detay'),
    path('feed/rss/', SonYazilarFeed(), name='rss'),
]
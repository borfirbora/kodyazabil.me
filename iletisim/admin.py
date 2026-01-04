from django.contrib import admin
from .models import Mesaj

@admin.register(Mesaj)
class MesajAdmin(admin.ModelAdmin):
    list_display = ('isim', 'konu', 'email', 'tarih', 'okundu')
    list_filter = ('okundu', 'tarih')
    search_fields = ('isim', 'mesaj', 'email')
    
    # Mesajlar admin panelinde sadece okunur olsun (readonly)
    readonly_fields = ('isim', 'email', 'konu', 'mesaj', 'tarih')
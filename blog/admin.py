from django.contrib import admin
from .models import Yazilar

@admin.register(Yazilar)
class YazilarAdmin(admin.ModelAdmin):
    list_display = ('baslik', 'olusturulma_tarihi', 'yayinda_mi')
    list_filter = ('yayinda_mi', 'olusturulma_tarihi')
    search_fields = ('baslik', 'icerik')
    # Başlığa göre slug'ı otomatik doldur
    prepopulated_fields = {'slug': ('baslik',)}
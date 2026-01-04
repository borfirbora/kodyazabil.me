from django.contrib import admin
from .models import Kategori, Egitim

@admin.register(Kategori)
class KategoriAdmin(admin.ModelAdmin):
    # Slug alanını isimden otomatik oluşturur
    prepopulated_fields = {'slug': ('isim',)}

@admin.register(Egitim)
class EgitimAdmin(admin.ModelAdmin):
    list_display = ('baslik', 'kategori', 'aktif', 'olusturulma_tarihi')
    list_filter = ('aktif', 'kategori')
    search_fields = ('baslik', 'aciklama')
    # Slug alanını başlıktan otomatik oluşturur
    prepopulated_fields = {'slug': ('baslik',)}
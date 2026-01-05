from django.contrib import admin
from .models import Proje

@admin.register(Proje)
class ProjeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('baslik',)}
    list_display = ('baslik', 'teknolojiler', 'olusturulma_tarihi')
    search_fields = ('baslik', 'teknolojiler')
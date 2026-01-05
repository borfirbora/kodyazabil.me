from django.db import models
from ckeditor.fields import RichTextField # <-- Import et

class Kategori(models.Model):
    isim = models.CharField(max_length=100, verbose_name="Kategori Adı")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="URL Yolu (Slug)")
    # slug: Adres çubuğunda görünür (orn: /egitimler/python-dersleri/)

    class Meta:
        verbose_name = "Kategori"
        verbose_name_plural = "Kategoriler"

    def __str__(self):
        return self.isim


class Egitim(models.Model):
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, related_name="egitimler", verbose_name="Kategori")
    baslik = models.CharField(max_length=200, verbose_name="Eğitim Başlığı")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="URL Yolu")
    aciklama = RichTextField(verbose_name="Kısa Açıklama", blank=True)
    # Resim alanı şimdilik opsiyonel olsun (blank=True)
    resim = models.ImageField(upload_to="egitim_resimleri/", blank=True, null=True, verbose_name="Kapak Resmi")
    aktif = models.BooleanField(default=True, verbose_name="Yayında mı?")
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Eğitim"
        verbose_name_plural = "Eğitimler"

    def __str__(self):
        return self.baslik
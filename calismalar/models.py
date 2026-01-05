from django.db import models
from ckeditor.fields import RichTextField # <-- Import et
class Proje(models.Model):
    baslik = models.CharField(max_length=200, verbose_name="Proje Adı")
    aciklama = RichTextField(verbose_name="Proje Açıklaması")
    resim = models.ImageField(upload_to="proje_resimleri/", verbose_name="Proje Görseli")
    
    # Yeni Alanlar: Linkler (Boş bırakılabilir, çünkü her projenin linki olmayabilir)
    github_link = models.URLField(blank=True, verbose_name="GitHub Linki")
    demo_link = models.URLField(blank=True, verbose_name="Canlı Önizleme Linki")
    slug = models.SlugField(unique=True, blank=True)
    teknolojiler = models.CharField(max_length=200, verbose_name="Kullanılan Teknolojiler", help_text="Örn: Python, Django, Tailwind")
    
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Proje"
        verbose_name_plural = "Projeler"
        ordering = ['-olusturulma_tarihi'] # En yenisi en üstte görünsün

    def __str__(self):
        return self.baslik
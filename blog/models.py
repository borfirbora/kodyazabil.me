from django.db import models
from ckeditor.fields import RichTextField
class Yazilar(models.Model):
    baslik = models.CharField(max_length=200, verbose_name="Yazı Başlığı")
    slug = models.SlugField(unique=True, null=True, verbose_name="URL Yolu")
    resim = models.ImageField(upload_to='blog/', blank=True, null=True, verbose_name="Kapak Görseli")
    icerik = RichTextField(verbose_name="Yazı İçeriği")
    ozet = RichTextField(max_length=300, blank=True, help_text="Listede görünecek kısa açıklama")
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)
    yayinda_mi = models.BooleanField(default=True, verbose_name="Yayında mı?")

    class Meta:
        verbose_name = "Blog Yazısı"
        verbose_name_plural = "Blog Yazıları"
        ordering = ['-olusturulma_tarihi'] # En yeni en üstte

    def __str__(self):
        return self.baslik
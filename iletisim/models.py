from django.db import models

class Mesaj(models.Model):
    isim = models.CharField(max_length=100, verbose_name="Gönderen Kişi")
    email = models.EmailField(verbose_name="E-posta Adresi")
    konu = models.CharField(max_length=200, verbose_name="Mesaj Konusu")
    mesaj = models.TextField(verbose_name="Mesaj İçeriği")
    
    okundu = models.BooleanField(default=False, verbose_name="Okundu mu?")
    tarih = models.DateTimeField(auto_now_add=True, verbose_name="Gönderilme Tarihi")

    class Meta:
        verbose_name = "Gelen Mesaj"
        verbose_name_plural = "Gelen Mesajlar"
        ordering = ['-tarih'] # En yeni mesaj en üstte

    def __str__(self):
        return f"{self.isim} - {self.konu}"
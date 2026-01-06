from django.contrib.syndication.views import Feed
from django.urls import reverse
from django.utils.html import strip_tags
from .models import Yazilar

class SonYazilarFeed(Feed):
    title = "Kodyazabil.me - Blog Yazıları"
    link = "/blog/"
    description = "Bora FIRLANGEÇ tarafından paylaşılan son blog yazıları ve notlar."

    def items(self):
        # Sadece yayında olan son 10 yazıyı getir
        return Yazilar.objects.filter(yayinda_mi=True).order_by('-olusturulma_tarihi')[:10]

    def item_title(self, item):
        return item.baslik

    def item_description(self, item):
        # Varsa özeti kullan, yoksa içeriğin HTML'ini temizleyip ilk 30 kelimeyi al
        if item.ozet:
            return item.ozet
        return strip_tags(item.icerik)[:200] + "..."

    def item_link(self, item):
        return reverse('blog:detay', kwargs={'slug': item.slug})
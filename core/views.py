from django.shortcuts import render
from django.db.models import Q
from egitimler.models import Egitim
from calismalar.models import Proje # Proje modelini de çağırdık

def anasayfa(request):
    # EĞİTİMLER: Sadece son 3 tanesi ([:3] dilimleme işlemi)
    egitimler = Egitim.objects.filter(aktif=True).order_by('-olusturulma_tarihi')[:3]

    # PROJELER: Sadece son 3 tanesi
    projeler = Proje.objects.all().order_by('-olusturulma_tarihi')[:3]

    context = {
        'egitimler': egitimler,
        'projeler': projeler
    }

    return render(request, 'core/anasayfa.html', context)

def arama(request):
    query = request.GET.get('q') # URL'den 'q' parametresini al (?q=python)
    egitim_sonuclari = []
    proje_sonuclari = []

    if query:
        # EĞİTİMLERDE ARA: Başlıkta VEYA Açıklamada geçenleri bul
        # icontains: Büyük/küçük harf duyarsız arama
        egitim_sonuclari = Egitim.objects.filter(
            Q(baslik__icontains=query) | Q(aciklama__icontains=query),
            aktif=True
        )

        # PROJELERDE ARA: Başlıkta, Açıklamada VEYA Teknolojilerde geçenleri bul
        proje_sonuclari = Proje.objects.filter(
            Q(baslik__icontains=query) | 
            Q(aciklama__icontains=query) |
            Q(teknolojiler__icontains=query)
        )

    context = {
        'query': query,
        'egitim_sonuclari': egitim_sonuclari,
        'proje_sonuclari': proje_sonuclari,
    }

    return render(request, 'core/arama_sonuclari.html', context)

def hakkimda(request):
    return render(request, 'core/hakkimda.html')
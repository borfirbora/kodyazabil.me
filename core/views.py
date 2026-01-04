from django.shortcuts import render
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
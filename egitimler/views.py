from django.shortcuts import render, get_object_or_404
from .models import Egitim

def tum_egitimler(request):
    # [:3] YOK! Hepsini getiriyoruz.
    egitimler = Egitim.objects.filter(aktif=True).order_by('-olusturulma_tarihi')
    return render(request, 'egitimler/tum_egitimler.html', {'egitimler': egitimler})

def egitim_detay(request, slug):
    # get_object_or_404: 
    # Bu slug'a sahip bir eğitim varsa getir, yoksa (biri adresi salladıysa) 
    # '404 Sayfa Bulunamadı' hatası ver.
    egitim = get_object_or_404(Egitim, slug=slug, aktif=True)

    context = {
        'egitim': egitim
    }
    
    return render(request, 'egitimler/detay.html', context)
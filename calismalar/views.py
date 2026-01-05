from django.shortcuts import render, get_object_or_404
from .models import Proje

def tum_projeler(request):
    projeler = Proje.objects.all().order_by('-olusturulma_tarihi')
    return render(request, 'calismalar/tum_projeler.html', {'projeler': projeler})

def calismalar_detay(request, slug):
    # Eğer slug bulunamazsa 404 hatası verir (sayfa patlamaz)
    proje = get_object_or_404(Proje, slug=slug)
    return render(request, 'calismalar/detay.html', {'proje': proje})
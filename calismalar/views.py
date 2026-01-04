from django.shortcuts import render
from .models import Proje

def tum_projeler(request):
    projeler = Proje.objects.all().order_by('-olusturulma_tarihi')
    return render(request, 'calismalar/tum_projeler.html', {'projeler': projeler})
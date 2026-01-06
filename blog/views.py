from django.shortcuts import render, get_object_or_404
from .models import Yazilar
from django.core.paginator import Paginator

def blog_liste(request):
    # Tüm yazıları al
    yazi_listesi = Yazilar.objects.filter(yayinda_mi=True)
    
    # 2. Sayfalayıcıyı Kur: Her sayfada 6 yazı olsun dedik
    paginator = Paginator(yazi_listesi, 6) 
    
    # URL'den sayfa numarasını al (Örn: ?page=2)
    sayfa_no = request.GET.get('page')
    
    # O sayfanın yazılarını getir
    yazilar = paginator.get_page(sayfa_no)
    
    return render(request, 'blog/liste.html', {'yazilar': yazilar})

def blog_detay(request, slug):
    yazi = get_object_or_404(Yazilar, slug=slug, yayinda_mi=True)
    return render(request, 'blog/detay.html', {'yazi': yazi})
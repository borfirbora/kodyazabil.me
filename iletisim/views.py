from django.shortcuts import render, redirect
from django.contrib import messages # Kullanıcıya uyarı göstermek için
from .forms import IletisimForm

def iletisim_sayfasi(request):
    if request.method == 'POST':
        # Kullanıcı butona bastıysa:
        form = IletisimForm(request.POST)
        if form.is_valid():
            form.save() # Mesajı veritabanına kaydet
            # Başarı mesajı ekle (Base.html'de görünür)
            messages.success(request, 'Mesajınız başarıyla gönderildi! En kısa sürede döneceğim.')
            return redirect('iletisim:sayfa') # Sayfayı yenile (tekrar form göndermeyi önler)
    else:
        # Sayfa ilk kez açılıyorsa boş form göster
        form = IletisimForm()

    return render(request, 'iletisim/iletisim.html', {'form': form})
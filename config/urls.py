from django.contrib import admin
from django.urls import path, include
# Bu ikisini ekle:
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', include('egitimler.urls')),
    path('calismalar/', include('calismalar.urls')),
    path('iletisim/', include('iletisim.urls')),
    path('blog/', include('blog.urls')),
]

# SADECE DEBUG MODUNDA: Medya dosyalarını sun
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)